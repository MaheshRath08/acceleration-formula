try:
    initial_velocity = float(input("Initial Velocity(in m/s):\n"))
    final_velocity = float(input("Final velocity(in m/s):\n"))
    elapsed_time = float(input("Elapsed Time(in s):\n"))
    acceleration = (final_velocity - initial_velocity)/elapsed_time
    print("Accelaration is "+str(acceleration))
except ValueError:
    print("Please type in numerical values")