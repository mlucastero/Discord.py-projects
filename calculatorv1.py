while True:
    print("----------------------------------------------------")
    def calculate():
        operation = input('''
    + : Cộng
    - : Trừ
    * : Nhân
    / : Chia
    hcn : Diện tính và chu vi hình chữ nhật
    hv : Diện tích và chu vi hình vuông
    csf : Đổi độ C sang F
    fsc : Đổi độ F sang C
    l : Tính độ dài text nhập vào
    -----CTRL C để thoát-----

    Nhập lựa chọn của bạn: ''')


        if operation == '+':
            print("============================")
            sohang1 = float(input("Nhập số của bạn: "))
            sohang2 = float(input("Nhập số của bạn: "))
            print('{} + {} = '.format(sohang1, sohang2))
            print(sohang1 + sohang2)


        elif operation == '':
            print("============================")
            sobitru = float(input("Nhập số của bạn: "))
            sotru = float(input("Nhập số của bạn: "))
            print('{} - {} = '.format(sobitru, sotru))
            print(sobitru - sotru)
        
        
        elif operation == '*':
            print("============================")
            tich1 = float(input("Nhập số của bạn: "))
            tich2 = float(input("Nhập số của bạn: "))
            print('{} * {} = '.format(tich1, tich2))
            print(tich1 * tich2)
       
       
        elif operation == '/':
            print("============================")
            sobichia = float(input("Nhập số của bạn: "))
            sochia = float(input("Nhập số của bạn: "))
            print('{} / {} = '.format(sobichia, sochia))
            print(sobichia / sochia)
        
        
        elif operation == 'hcn':
            print("============================")
            length = float(input("Chiều dài là: "))
            width = float(input("Chieu rong laà "))
            print("Chiều dài hinh chữ nhật là:" + str(length))
            print("Chiều rộng hình chữ nhật là:" + str(width))
            print("Chu vi hình chữ nhật là:" , (float(length) + float(width)) * 2)
            print("Diện tích là:  ", float(length) * float(width))
        
        
        elif operation == 'hv':
            print("============================")
            side = float(input("Cạnh là "))
            print("Cạnh là: " + str(side))
            print("Chu vi hình vuông là: " , float(side) * 4)
            print("Diện tích hình vuông là: ", float(side) * float(side))
        
        
        elif operation == 'csf':
            print("============================")
            Celsius = float(input("Nhập độ C: "))
            print(str(Celsius) + " Độ C = ",Celsius * 1.8 + 32, "Độ F")
        
        
        elif operation == 'fsc':
            print("============================")
            Fahrenheit = float(input("Nhập độ F: "))
            print( str(Fahrenheit) + " Độ F = " ,Fahrenheit - 32 / 1.8 , "Độ C")


        elif operation == 'l': 
            print("============================")
            text = input("Nhập text của bạn: ")
            print("Độ dài là: " + str(len(text)))



        

        else:
            print("=================================================")
            print('Tôi không hiểu')
    calculate()
    print("=================================================")
    print("")
    print("")
