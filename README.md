# ComputerV1
## Description
The goal of this project is to  code a simple equation solving program, 
It will take polynomial equations into account.
These equations will only require exponents. No complex function.
Why polynomials? Just because it’s one of the simplest and most powerful tools in
mathematics. It is used in every field on every level to simplify and express many things.
For instance, they help calculate functions such as sin, cos, et tan.



## Usage

```python 
# run command bellow
python computerv1.py
#you will be prompted to enter an equation to solve
give me an equation to solve:(write your equation her)
#example:
give me an equation to solve:1 * X^0  - 4 * X^1 + 2 *  X^2 = 1 * X^0 - 1* X^1 
#expected output
Polynomial degree:  1
Reduced form:   - 3 * X^1 + 2 * X^2 = 0
Discriminant strictly positive ,the two solutions are:
0.0
1.5

```
## Note:
- The program is  only able to solve a polynomial second or lower degree equations, you will get an error message for higher degree equations.
- The program expect the entry to have the right format, ie. every term respect the
form a ∗ x^p.
- Exponents are organized(from lower to higher) and present
