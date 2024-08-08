# Task: Create functions that approximate the first derivative using the central difference method, and visualize the accuracy for various step sizes on a given interval.

# 1. Import the necessary plotting package.



# 2. Define a function called central_difference that takes a function f, a point x, and a small value h as input,
# and outputs the approximate first derivative of f at x using the central difference method.



# 3. Import the numpy package under the correct alias.



# 4. The function below takes in the original function, its true derivative, an interval of x-values in the form of a 2-element list, and list of h-values.
# It will plot the true first derivative on the interval as well as the approximations for different h-values.
# Finish the function definition below by completing the four TO DOs.

def plot_derivative_approximations(func, true_derivative, interval, h_values):

    # TODO: Define a list called x_values that contains 1000 equally spaced values spanning the given interval (use numpy).


    
    # TODO: Define a list called true_derivatives that contains the true derivative at each value in x_values.

    

    plt.figure(figsize=(14, 8))
  
    # TODO: Plot the true derivative in the color black with the label True Derivative.

  

    # TODO: For each h-value, define a list called approx_derivatives that approximates the true
    # derivative using the central difference method (with the given h-value) at each x-value in
    # x_values. Then plot the approximate derivative and give it the label Approx Derivative (h=#)
    # where # should be replaced with the corresponding value of h.


    plt.xlabel('x')
    plt.ylabel('Derivative')
    plt.title('First Derivative Approximation Using Central Difference Method')
    plt.legend()
    plt.grid(True)
    plt.show()
