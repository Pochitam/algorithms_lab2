import time
import matplotlib.pyplot as plt
import algorithms
import generateData


def measure_time(num_rec):
    time_perebprchik = []
    time_karta_built = []
    time_karta = []
    time_pst_built = []
    time_pst = []
    time_karta_and_built = []
    time_pst_and_built = []

    for n in num_rec:
        print(f'Шаг {n}')
        rectangles = generateData.generate_rectangles(n, 10)
        points = generateData.generate_points(n, n)

        #замерчик переборчика
        start_time = time.time()
        for x, y in points:
            algorithms.pereborchik(rectangles, x, y)
        time_perebprchik.append(time.time() - start_time)

        #замерчик карты с подготовкой
        start_time = time.time()
        matrix, arr_x, arr_y = algorithms.karta_prepare(rectangles)
        time_karta_built.append(time.time()-start_time)
        start_time_2 = time.time()
        for x, y in points:
            algorithms.karta(matrix, arr_x, arr_y, x, y)
        time_karta.append(time.time() - start_time_2)
        time_karta_and_built.append(time.time() - start_time)

        #замерчик дерева с подготовкой
        start_time = time.time()
        pst, lst_x, lst_y = algorithms.pst_prepare(rectangles)
        time_pst_built.append(time.time() - start_time)
        start_time_2 = time.time()
        for x, y in points:
            algorithms.pst(pst, lst_x, lst_y, x, y)
        time_pst.append(time.time() - start_time_2)
        time_pst_and_built.append(time.time() - start_time)
    return [time_perebprchik, time_karta_built, time_karta, time_pst_built, time_pst, time_karta_and_built, time_pst_and_built]

def measure_time_many_points(num):
    time_perebprchik = []
    time_karta = []
    time_pst = []
    rectangles = generateData.generate_rectangles(1000, 10)
    for n in num:
        points = generateData.generate_points(n, n)
        #замерчик переборчика
        start_time = time.time()
        for x, y in points:
            algorithms.pereborchik(rectangles, x, y)
        time_perebprchik.append(time.time() - start_time)

        #замерчик карты с подготовкой
        start_time = time.time()
        matrix, arr_x, arr_y = algorithms.karta_prepare(rectangles)
        for x, y in points:
            algorithms.karta(matrix, arr_x, arr_y, x, y)
        time_karta.append(time.time() - start_time)

        #замерчик дерева с подготовкой
        start_time = time.time()
        pst, lst_x, lst_y = algorithms.pst_prepare(rectangles)
        for x, y in points:
            algorithms.pst(pst, lst_x, lst_y, x, y)
        time_pst.append(time.time() - start_time)
    return [time_perebprchik, time_karta, time_pst]



def generate_graph_prepare(times):
    time_perebprchik, time_karta_built, time_karta, time_pst_built, time_pst, time_karta_and_built, time_pst_and_built = times
    plt.plot(num_recs, time_karta_built, label="Подготовка карты", color='red', marker='o')
    plt.plot(num_recs, time_pst_built, label="Подготовка дерева", color='green', marker='o')
    plt.xlabel('Кол-во прямоугольников и точек')
    plt.ylabel('Время выполнения')
    plt.title('График подготовки данных (карта и дерево)')
    plt.legend()
    plt.tight_layout()
    plt.yscale('log')
    plt.show()

def gen_graph_no_prepare(times):
    time_perebprchik, time_karta_built, time_karta, time_pst_built, time_pst, time_karta_and_built, time_pst_and_built = times
    plt.plot(num_recs, time_perebprchik, label="Перебор", color='blue', marker='o')
    plt.plot(num_recs, time_karta, label="Карта", color='red', marker='o')
    plt.plot(num_recs, time_pst, label="Персистентное дерево", color='green', marker='o')
    plt.xlabel('Кол-во прямоугольников и точек')
    plt.ylabel('Время выполнения')
    plt.title('График алгоритмов без учета подготовки данных')
    plt.legend()
    plt.tight_layout()
    plt.yscale('log')
    plt.show()

def gen_graph_with_prepare(times):
    time_perebprchik, time_karta_built, time_karta, time_pst_built, time_pst, time_karta_and_built, time_pst_and_built = times
    plt.plot(num_recs, time_perebprchik, label="Перебор", color='blue', marker='o')
    plt.plot(num_recs, time_karta_and_built, label="Карта", color='red', marker='o')
    plt.plot(num_recs, time_pst_and_built, label="Персистентное дерево", color='green', marker='o')
    plt.xlabel('Кол-во прямоугольников и точек')
    plt.ylabel('Время выполнения')
    plt.title('График алгоритмов с учетом подготовки данных')
    plt.legend()
    plt.tight_layout()
    plt.yscale('log')
    plt.show()

def gen_graph_with_many_points(times):
    time_perebprchik, time_karta, time_pst = times
    plt.plot(num_recs, time_perebprchik, label="Перебор", color='blue', marker='o')
    plt.plot(num_recs, time_karta, label="Карта", color='red', marker='o')
    plt.plot(num_recs, time_pst, label="Персистентное дерево", color='green', marker='o')
    plt.xlabel('Кол-во точек')
    plt.ylabel('Время выполнения')
    plt.title('График алгоритмов с учетом подготовки данных (1000 прямоугольников)')
    plt.legend()
    plt.tight_layout()
    plt.yscale('log')
    plt.show()

num_recs = [x for x in range(10, 2000, 100)]
times = measure_time(num_recs)
times2 = measure_time_many_points(num_recs)
print(num_recs, len(times))
gen_graph_with_many_points(times2)
