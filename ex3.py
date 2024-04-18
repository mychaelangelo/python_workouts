
# My solution
def run_timing():
    """
    Requests 10km run times until a user presses enter with a blank input.
    Result is the average run time.
    """
    num_list = []
    num = None
    while num != "":
        num = input("Enter 10 km run time: ")
        try:
            num_list.append(float(num))
        except:
            pass
    print(f"Average of {sum(num_list)/len(num_list)}, over {len(num_list)} runs")


if __name__ == "__main__":
    run_timing()