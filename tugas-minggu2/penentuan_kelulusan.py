kehadiran = int(input("Jumlah kehadiran(1-14): "))
nilai = int(input("Nilai Ujian (0-100): "))

if kehadiran >= 12:
    if nilai >= 75:
        print("LULUS - Nilai memuaskan")
    else:
        print ("REMEDIAL - Nilai Ujian kurang")
else:
    print("TIDAK LULUS - Kehadiran kurang dari 12")