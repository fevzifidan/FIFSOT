def num_gen(start:int = 0, zfill:int = 1, rev:bool = False):
    while True:
        yield str(start).zfill(zfill)
        if rev == True:
            start -= 1
        elif rev == False:
            start += 1
        else:
            raise Exception(f"Unidentified parameter 'rev'! >> {rev}")


# END