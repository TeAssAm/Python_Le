from time import sleep
class TrafficLight:
    color = ['Красный', 'Желтый', 'Зеленый']

    def running(self):
        i = 0
        print('Светофор начинает работать: ')
        while i < 3:
            print(f'{TrafficLight.color[i]}')
            if i == 0:
                sleep(7)
            elif i == 1:
                sleep(2)
            elif i == 2:
                sleep(20)
            i += 1

TrafficLight = TrafficLight()
TrafficLight.running()
