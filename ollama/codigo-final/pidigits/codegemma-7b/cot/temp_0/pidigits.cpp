**Chain-of-Thought Reasoning for Implementing the Unbounded Spigot Algorithm (Gibbons) in C++ to Compute Arbitrary-Precision Digits of Pi**

**1. Problem Decomposition:**

**a. Unbounded Spigot Algorithm:**

- The algorithm generates digits of pi by iteratively calculating `q` and `r`.
- `next_step()` updates these values based on the formula provided.
- `extract()` extracts a digit from `q` based on the current values of `q`, `r`, and `t`.
- `produce()` appends the extracted digit to the output and adjusts `r`.

**b. Digit Selection Logic:**

- The algorithm repeatedly calls `next_step()` until `q > r` is false.
- It then extracts the third digit (`d = extract(3)`) and checks if it matches the fourth digit (`extract(4)`).
- If they match, the digit is output; otherwise, `next_step()` is re-triggered.

**c. Arbitrary Precision Arithmetic:**

- The GMP library provides arbitrary-precision integers (`mpz_t`) for handling large numbers without overflow.

**2. Algorithm Implementation Steps:**

**a. Initialization:**

- Initialize the variables `q`, `r`, `t`, and `k` as per the problem description.

**b. `next_step()` Function:**

- Implements the exact formula provided in the problem.

**c. `extract()` Function:**

- Calculates the floor of `(q*x + r) / t`.

**d. `produce()` Function:**

- Appends the extracted digit to the output and adjusts `r`.

**3. Digit Verification:**

- After each digit output, compare `d` with `extract(4)` to ensure correctness.

**4. Output Formatting:**

- Print digits in groups of 10 per line, padding with spaces if necessary.
- Append `\t:N` to each line, where `N` is the input argument.

**5. GMP Integration:**

- Use `mpz_t` for all integer operations in the algorithm.

**6. Command-Line Handling:**

- Parse `N` from the command line argument.

**7. Edge Cases:**

- Handle cases where `q > r` is false early to avoid infinite loops.
- Pad trailing lines with spaces if necessary.

**Key Requirements:**

- Use GMP library for arbitrary-precision arithmetic.
- Follow the exact algorithm steps.
- Verify digit correctness.
- Format output as specified.
- Accept input from command line.
