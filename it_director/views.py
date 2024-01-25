from django.shortcuts import render
import requests
import re
from it_director.models import *


def main(request):
    main_results = MainBinary.objects.all()
    navigation = NavBinary.objects.all()
    context = {'main_results': main_results, 'navigation': navigation}
    return render(request, 'main.html', context)


def relevance(request):
    navigation = NavBinary.objects.all()
    relevance_results = RelevanceData.objects.all()
    context = {'relevance_results': relevance_results, 'navigation': navigation}
    return render(request, 'relevance.html', context)


def location(request):
    location_results = GeoData.objects.all()
    navigation = NavBinary.objects.all()
    context = {'navigation': navigation,
                         'location_results': location_results}
    return render(request, 'location.html', context)


def job_abilities(request):
    navigation = NavBinary.objects.all()
    job_abilities_results = SkillData.objects.all()
    context = {'navigation': navigation, 'job_abilities_results': job_abilities_results}
    return render(request, 'job_abilities.html', context)


def recent_jobs(request):
    navigation = NavBinary.objects.all()

    class HHAPI:

        def __init__(self, search_text: str):
            self.text = search_text

        def __get_full_vacancies__(self, date: str, count_vac: int) -> list:
            url = 'https://api.hh.ru/vacancies'
            return requests.get(url, dict(text=self.text,
                                          specialization=1,
                                          date_from=f"{date}T00:00:00",
                                          date_to=f"{date}T23:00:00",
                                          per_page=count_vac,
                                          page=1)).json()["items"]

        def get_data_vacancies(self, date: str, count_vac: int):
            data = self.__get_full_vacancies__(date, count_vac)
            result_list = []
            for vac in data:
                url_vac = f'https://api.hh.ru/vacancies/{vac["id"]}'
                resp = requests.get(url_vac).json()
                if resp['salary']:
                    description = ' '.join(re.sub(re.compile('<.*?>'), '', resp['description'])
                                           .strip()
                                           .split())
                    description = description[:2000] + '...' if len(description) >= 2000 else description
                    result_list.append({'name': resp['name'],
                                        'description': description,
                                        'key_skills': list(map(lambda x: x['name'], resp['key_skills'])),
                                        'employer': resp['employer']['name'],
                                        'salary': f"{resp['salary']['from']} - {resp['salary']['to']} {resp['salary']['currency']}",
                                        'area': resp['area']['name'],
                                        'published_at': resp['published_at'][:10],
                                        'alternate_url': resp['alternate_url']})

            return result_list

    last_vacancies = LatestApiVacancy.objects.all()
    for vacancy in last_vacancies:
        hh = HHAPI(vacancy.vacancy)
    vacs = hh.get_data_vacancies('2024-01-20', 10)


    context_last_vacancies = {'navigation': navigation,
                              'vacs': vacs, 'last_vacancies': last_vacancies}

    return render(request, 'recent_jobs.html', context_last_vacancies)
