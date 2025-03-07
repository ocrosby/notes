import marimo

__generated_with = "0.11.14"
app = marimo.App(width="medium")


@app.cell
def _():
    import marimo as mo

    return (mo,)


@app.cell
def _(mo):
    mo.md(
        r"""
        # Omar's Marimo Notes

        ## Markdown from Python

        In a Python cell you can create markdown as follows using marimo:

        ```python
        mo.md(`Hello World!`)
        ```

        If a marimo UI widget was previously created like a slider

        ```python
        slider = mo.ui.slider(1,22)
        ```

        you can call it out by name within a markdown block like this

        ```python
        mo.md(
            f\"""
            something really cool: {slider}
            \"""
        )
        ```

        from the example this is used to duplicate something multiple times in a H2 block

        ```python
        mo.md(
            f\"""
            something really cool: {slider}

            {"##" + "🍃" * slider.value}
            \"""
        )
        ```

        This would duplicate 🍃 in a H2 block however many times specified by the sliders value.

        That's pretty cool.

        ## The Marimo Accordion

        The Accordion is used to display a small description that can be expanded into a larger text block

        ```python
        mo.accordion(
            {
                "Tip: disabling automatic execution": mo.md(
                    rf\"""
                marimo lets you disable automatic execution: just go into the
                notebook settings and set

                "Runtime > On Cell Change" to "lazy".

                When the runtime is lazy, after running a cell, marimo marks its
                descendants as stale instead of automatically running them. The
                lazy runtime puts you in control over when cells are run, while
                still giving guarantees about the notebook state.
                \"""
                )
            }
        )
        ```

        Here you can see the tip first when the cell is executed but have the option to exand it to then see the markdown block that is associated with it.

        ## The Marimo Callout

        The callout appears as a bubble with rounded corners. It has a 3D effect associated with it to draw the users eyes to it.

        ```python
        mo.md(
            \"""
            Tip: This is a tutorial notebook. You can create your own notebooks
            by entering `marimo edit` at the command line.
            \"""
        ).callout()
        ```
        """
    )
    return


if __name__ == "__main__":
    app.run()
