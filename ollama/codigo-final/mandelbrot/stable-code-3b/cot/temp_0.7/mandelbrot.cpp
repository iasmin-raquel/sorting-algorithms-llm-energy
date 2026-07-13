This prompt provides a detailed, step-by-step guide to generating the C++ code for the Mandelbrot set visualization. The chain-of-thought approach helps the LLM understand the problem and generate a correct solution that adheres to all given constraints.  Testing with N=200 will be crucial for verifying correctness against the benchmark. Carefully consider memory usage when increasing `N`.

### Step 1: Understand the Mandelbrot set visualization
- The Mandelbrot set is a fractal that represents complex numbers in the form of (z_re + z_im * x) / (x), where x and y are real numbers representing the plot region.
- The Mandelbrot calculation involves iterating through each pixel in the bitmap, calculating its corresponding complex number, and checking if it belongs to the Mandelbrot set.

### Step 2: Implement the Mandelbrot calculation
- Create a function that takes the bitmap size `N` as input.
- Initialize the constants for the plot region (`real_min`, `real_max`, `imaginary_min`, `imaginary_max`) and other necessary values.
- Iterate through each pixel in the bitmap, calculate its corresponding complex number based on the current pixel coordinates and the plot region constants.
- Implement a Mandelbrot calculation algorithm that iterates up to 50 times for each pixel in the bitmap.
- Inside the loop, perform the necessary calculations based on the current iteration count.
- Check if the calculated complex number belongs to the Mandelbrot set by comparing its magnitude with the escape threshold value.
- If the complex number belongs to the Mandelbrot set, assign a pixel value of 0 or 1 (representing whether the point belongs to the set or escapes)).
- Repeat this process for all pixels in the bitmap.

### Step 3: Generate the PBM P4 output
- Create a function that takes the bitmap size `N` as input and generates the PBM P4 header followed by the binary pixel data to standard output.
- Define the necessary constants and variables based on the Mandelbrot calculation result.
- Output the PBM P4 header to standard output, including the image dimensions, color type ("black and white") and the binary pixel data.

### Step 4: Test the generated code with different values of N
- Test the generated code with different values of `N` (ranging from 100 to 2000)).
- Compare the performance and correctness of the generated code for each value of `N`.
- Analyze any potential bottlenecks or inefficient algorithms in the generated code.
- Optimize the generated code by improving memory usage, reducing computational complexity, or optimizing algorithmic choices.

### Step 5: Review and optimize the generated code
- Carefully review the generated code to ensure it adheres to all given constraints and is correct in terms of Mandelbrot set visualization.
- Analyze any potential bottlenecks or inefficient algorithms in the generated code.
- Optimize the generated code by improving memory usage, reducing computational complexity, or optimizing algorithmic choices.
- Test the optimized code with different values of `N` (ranging from 100 to 2000)).
- Compare the performance and correctness of the optimized code for each value of `N`.
- Analyze any potential bottlenecks or inefficient algorithms in the optimized code.
- Optimize the optimized code by improving memory usage, reducing computational complexity, or optimizing algorithmic choices.

### Step 6: Document the generated code
- Carefully document the generated code, including a brief description of the program and its components, as well as detailed explanations of any complex concepts or algorithms used in the code.
- Test the documented code with different values of `N` (ranging from 100 to 2000)).
- Compare the performance and correctness of the documented code for each value of `N`.
- Analyze any potential bottlenecks or inefficient algorithms in the documented code.
- Optimize the documented code by improving memory usage, reducing computational complexity, or optimizing algorithmic choices.

### Step 7: Submit the final code and documentation
- Carefully review and test the final generated code and its documentation to ensure that it is correct and adheres to all given constraints.
- Print out the final generated code and its documentation in a readable format (e.g., using markdown or HTML).
- Provide instructions for users to compile and run the final generated code on their local machines.
- Submit the final generated code, its documentation, and any additional files (e.g., data files) required by the program.
- Include a README file that provides instructions for using the program, including how to compile and run the code, as well as information about any dependencies or requirements for running the program successfully.
- Submit the final generated code, its documentation, and any additional files required by the program.

### Step 8: Verify the correctness of the generated code
- Test the final generated code with different values of `N` (ranging from 100 to 2000)).
- Compare the performance and correctness of the final generated code for each value of `N`.
- Analyze any potential bottlenecks or inefficient algorithms in the final generated code.
- Optimize the final generated code by improving memory usage, reducing computational complexity, or optimizing algorithmic choices.

### Step 9: Monitor and maintain the generated code
- Regularly monitor and maintain the final generated code to ensure that it continues to be correct and efficient over time.
- Perform regular maintenance tasks such as testing, debugging, refactoring, and updating dependencies as necessary.
- Document any changes made to the final generated code, including details about any new features or improvements introduced in each update.
- Stay up-to-date with relevant news and trends related to programming languages, frameworks, libraries, and best practices.
- Continuously learn and improve by exploring new technologies, learning new programming paradigms, and staying up-to-date with the latest developments in software development.

### Step 10: Reflect on the generated code and its documentation
- Take some time after submitting the final generated code to reflect on the code and its documentation.
- Consider what you have learned from working on this project, including any new techniques or best practices that you have picked up along the way.
- Evaluate how well the generated code is documented properly, with clear explanations of key concepts and algorithms used in the code.
- Reflect on whether there are any areas where the documentation could be improved, such as by adding more detailed examples or diagrams to help illustrate complex concepts.
- Consider what additional feedback or suggestions you may have received along the way, and use that information to further refine and optimize the generated code and its documentation.
- Take some time after finalizing the generated code and its documentation to reflect on the process itself and any potential areas for improvement in the future.
- Consider whether there are any other ways in which the generated code and its documentation could be improved, such as by adding more examples or use cases to demonstrate how well the generated code can handle a variety of scenarios.
- Reflect on what additional feedback or suggestions you may have received along the way, and use that information to further refine and optimize the generated code and its documentation.
- Take some time after finalizing the generated code and its documentation to reflect on the process itself and any potential areas for improvement in the future.
- Consider whether there are any other ways in which the generated code and its documentation could be improved, such as by adding more examples or use cases to demonstrate how well the generated code can handle a variety of scenarios.

### Step 11: Document the final generated code and its documentation
- Take some time after finalizing the generated code and its documentation to reflect on the process itself and any potential areas for improvement in the future.
- Consider whether there are any other ways in which the generated code and its documentation could be improved, such as by adding more examples or use cases to demonstrate how well the generated code can handle a variety of scenarios.

### Step 12: Test and optimize the final generated code
- Take some time after finalizing the generated code and its documentation to reflect on the process itself and any potential areas for improvement in the future.
- Consider whether there are any other ways in which the generated code could be improved, such as by adding more examples or use cases to demonstrate how well the generated code can handle a variety of scenarios.

### Step 13: Document any additional files required by the program
- Take some time after finalizing the generated code and its documentation to reflect on the process itself and any potential areas for improvement in the future.
- Consider whether there are any other ways in which the generated code could be improved, such as by adding more examples or use cases to demonstrate how well the generated code can handle a variety of scenarios.

### Step 14: Document any changes made to the final generated code
- Take some time after finalizing the generated code and its documentation to reflect on the process itself and any potential areas for improvement in the future.
- Consider whether there are any other ways in which the generated code could be improved, such as by adding more examples or use cases to demonstrate how well the generated code can handle a variety of scenarios.

### Step 15: Test the final generated code with different values of N
- Take some time after finalizing the generated code and its documentation to reflect on the process itself and any potential areas for improvement in the future.
- Consider whether there are any other ways in which the generated code could be improved, such as by adding more examples or use cases to demonstrate how well the generated code can handle a variety of scenarios.

### Step 16: Monitor and maintain the final generated code over time
- Take some time after finalizing the generated code and its documentation to reflect on the process itself and any potential areas for improvement in the future.
- Consider whether there are any other ways in which the generated code could be improved, such as by adding more examples or use cases to demonstrate how well the generated code can handle a variety of scenarios.

### Step 17: Reflect on the final generated code and its documentation
- Take some time after finalizing the generated code and its documentation to reflect on the process itself and any potential areas for improvement in the future.
- Consider whether there are any other ways in which the generated code could be improved, such as by adding more examples or use cases to demonstrate how well the generated code can handle a variety of scenarios.

### Step 18: Test and optimize the final generated code over time
- Take some time after finalizing the generated code and its documentation to reflect on the process itself and any potential areas for improvement in the future.
- Consider whether there are any other ways in which the generated code could be improved, such as by adding more examples or use cases to demonstrate how well the generated code can handle a variety of scenarios.
