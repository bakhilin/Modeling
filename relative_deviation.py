generated_data_m = [67.71, 85.91,77.88,69.5,75.63]
main_data_m = [40.703,47.187,65.811,71.087,72.21]

generated_data_dispersia = [4923.503,6558.562,4852.912,6296.523,8736.69]
main_data_dispersia = [11173.52,1212.68,3941.97,5483.81,5305.516]

generated_data_sko = [70.16,80.98,69.66,79.35,93.47]
main_data_sko = [34.25,34.82,62.785,74.05,72.83]

generated_data_kt = [103.622,94.25,89.43,114.15,123.58]
main_data_kt = [84.16,73.79,95.40,104.17,100.87]

generated_data_09 = [40.674,31.31,16.51,13.17,10.92]
main_data_09 = [19.85,13.46,14.88,12.29,8.51]

generated_data_095 = [50.194,37.9,19.79,15.744,13.03]
main_data_095 = [24.50,16.297,17.84,14.69,10.15]

generated_data_099 = [72.11,51.8,26.4,20.84,17.18]
main_data_099 = [35.205,22.27,23.79,19.44,13.39]

sdvig = [10,20,50,100,200]

def deviation(name, gen_data, main_data):
    print(name)
    for i in range(len(sdvig)):
        result = (gen_data[i]-main_data[i]) / main_data[i]
        print(sdvig[i],result*100)


if __name__ == '__main__':
    deviation('мат ожидание %', generated_data_m, main_data_m)
    deviation('Дисперсия %', generated_data_dispersia, main_data_dispersia)
    deviation('СКО %', generated_data_sko, main_data_sko)
    deviation('КТ вариации %', generated_data_kt, main_data_kt)
    deviation('Дов инт 0.9 %', generated_data_09, main_data_09)
    deviation('Дов инт 0.95 %',generated_data_095, main_data_095)
    deviation('Дов инт 0.99 %', generated_data_099, main_data_099)
