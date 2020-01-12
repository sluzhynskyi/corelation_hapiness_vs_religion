with open("../data_demo/happiness_2015.csv") as f_r:
    with open("../data_demo/religion_2015.csv") as f_h:
        with open("../data/religion.csv", "w+") as f_r_out:
            with open("../data/happiness.csv", "w+") as f_h_out:
                print(f_r.readline(), file=f_r_out, end="")
                print(f_h.readline(), file=f_h_out, end="")
                try:
                    for line_r in f_r:
                        f_h.seek(0)
                        f_h.readline()
                        for line_h in f_h:
                            if line_r.split(",")[0] == line_h.split(",")[0]:
                                print(line_r, file=f_r_out, end="")
                                print(line_h, file=f_h_out, end="")
                                break
                except EOFError:
                    pass
