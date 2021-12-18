code = input()
out_f = open("output.txt", "w")
pyfuck = "exec("
pyfuck += "+".join([f"chr({'+1'*ord(c)})" for c in code])
pyfuck += ")"

for p in pyfuck:
    if p not in "exchr(+1)":
        print("Error:exchr(+1)")
        pyfuck = ""
        break

out_f.write(pyfuck)
out_f.close()