def game_core_v3(number):
    '''Делим диапазон предсказанием пополам. Проверяем попадание загаданного числа в верхнюю или нижнюю половину и отбрасываем пустую.
       Повторяем до точного попадания или до разницы между загаданным и предсказанным числом в единицу.
       Функция принимает загаданное число и возвращает число попыток'''
    count = 1
    bottom = 1
    top = 100
    predict = (top - bottom)//2
    while number != predict:
        if number > predict:
            count+=1
            bottom = predict
            predict += (top - bottom)//2
            if (number - predict) == 1:
                count+=1
                predict += 1
        elif number < predict:
            count+=1
            top = predict
            predict -= (top - bottom)//2
            if (predict - number) == 1:
                count+=1
                predict -= 1
        return(count) # выход из цикла, если угадали

def score_game(game_core):
    '''Запускаем игру 1000 раз, чтобы узнать, как быстро игра угадывает число'''
    count_ls = []
    np.random.seed(1)  # фиксируем RANDOM SEED, чтобы ваш эксперимент был воспроизводим!
    random_array = np.random.randint(1,101, size=(1000))
    for number in random_array:
        count_ls.append(game_core(number))
    score = int(np.mean(count_ls))
    print("Данный алгоритм угадывает число в среднем за ", score, "попыток")
    
import numpy as np
number = np.random.randint(1,101)   # загадали число
print ("Загадано число от 1 до 100")
score_game(game_core_v3)
