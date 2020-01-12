with open("demo_data/national_religions.csv") as f:
    with open("data/religion_2015.csv", "w+") as f_out:
        print(f.readline(), file=f_out, end="")
        for line in f:
            if line.startswith("2010,"):
                print(line[5:], file=f_out, end="")
