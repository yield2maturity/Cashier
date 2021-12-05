def diskon(total_harga):
    if total_harga>50000:
        diskon=0.1
    elif total_harga>20000:
        diskon=0.05
    else:
        diskon=0
    return diskon

var_diskon = diskon(50000)

