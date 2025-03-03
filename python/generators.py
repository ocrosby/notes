import marimo

__generated_with = "0.10.17"
app = marimo.App(width="medium")


@app.cell
def _():
    import marimo as mo
    return (mo,)


@app.cell
def _(mo):
    mo.md(
        r"""
        Generators are a special kind of iterator that are defined using a function. 
        They are created using the `yield` keyword instead of `return`. When a generator is called, 
        it returns an iterator object but does not start execution immediately. The function is 
        executed only when the `next()` method is called on the iterator object. The generator 
        function can pause and resume its execution, allowing it to produce a sequence of values
        over time.

        Here is an example of a simple generator function:
        """
    )
    return


@app.cell
def first_generator():
    def my_generator():
        yield 1
        yield 2
        yield 3
        yield 4

    return (my_generator,)


@app.cell
def _(my_generator):
    def use_next_with_generator():
        gen = my_generator()
        
        print(next(gen))  # Output: 1
        print(next(gen))  # Output: 2
        print(next(gen))  # Output: 3

    use_next_with_generator()
    return (use_next_with_generator,)


@app.cell
def _(my_generator):
    def display_generated_elements():
        gen = my_generator()
        
        for item in gen:
            print(item)

        return


    display_generated_elements()
    return (display_generated_elements,)


@app.cell
def _():
    return


if __name__ == "__main__":
    app.run()
