from httprequest import get_html
import json


class TramStop:
    def __init__(self, name):
        self.name = name

    def get_stop_info(self) -> str:
        url = f"http://www.ttss.krakow.pl/internetservice/geoserviceDispatcher/services/stopinfo/stops?left=-648000000&bottom=-324000000&right=648000000&top=324000000"
        tram_list = open("tram_list.json", "w")
        tram_list.write(get_html(url))
        tram_list.close()

        with open("tram_list.json") as tram_list:
            parsed_tram_list = json.load(tram_list)


        stops = parsed_tram_list['stops']

        for stop in stops:
            if stop['name'] == self.name:
                stop_id = stop['shortName']
                stop_info = open("stop_info.json", "w")
                stop_info.write(get_html(f"http://www.ttss.krakow.pl/internetservice/services/passageInfo/stopPassages/stop?stop={stop_id}"))
                stop_info.close()

                with open("stop_info.json") as stop_info:
                    parsed_stop_info = json.load(stop_info)
                trams = parsed_stop_info['actual']
                result = ""
                for tram in trams:
                    result += f"Linia: {tram['patternText']}, Kierunek: {tram['direction']}, Przyjazd: {tram['plannedTime']}\n"
                return result


