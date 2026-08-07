**Chain-of-Thought Reasoning for Implementing the Unbounded Spigot Algorithm in Java to Compute N Digits of Pi:**

**1. Understand the Problem Requirements:**

- The goal is to implement a Java program using `BigInteger` to compute the first *N* digits of π.
- The output should be formatted with 10 digits per line, padded with spaces, followed by `\t:N`.

**2. Decompose the Algorithm:**

- Initialize variables `q`, `r`, `t`, and `k`.
- Implement the `next_step()` function to update these variables according to the Spigot algorithm.
- Define `extract(x)` to calculate `(q*x + r) / t` using `BigInteger`.
- Implement `produce(d)` to update `q` and `r` for digit extraction.

**3. Digit Selection Logic:**

- Loop until `q > r` is false.
- Extract the digit `d` using `extract(3)`.
- Verify `d` using `extract(4)`.
- If valid, output the digit and call `produce(d)`.
- Otherwise, call `next_step()` to continue the algorithm.

**4. Output Formatting:**

- Collect 10 digits at a time.
- Pad with spaces if necessary.
- Append `\t:N` where *N* is the total digits calculated.

**5. Java-Specific Constraints:**

- Use `BigInteger` for all calculations.
- Parse *N* from the command line as an integer.

**6. Edge Cases & Validation:**

- Handle invalid or zero *N*.
- Ensure the algorithm terminates when `q > r` is false.

**7. Code Structure:**

- Main method:
    - Initialize variables.
    - Call the digit selection loop.
    - Print results in the specified format.

**Key Requirements:**

- Use `BigInteger` for calculations.
- Follow the Unbounded Spigot algorithm exactly.
- Verify digits using `extract(4)`.
- Output in the correct format.
- Handle edge cases.

**Notes:**

- Clarify if the LLM expects the safeguard against `extract(4)` violation.
- Optimize for correctness over raw speed.
- Provide a reference file for *N = 30* for comparison.
