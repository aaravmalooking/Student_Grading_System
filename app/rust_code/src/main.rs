mod interface;
mod help;


use pyo3::prelude::*;

fn main() {
    interface::main()

    // pyo3::prepare_freethreaded_python();
    //
    // // Initialize the Python interpreter
    // Python::with_gil(|py|{
    //
    //     let sys = py.import("sys")?;
    //
    //
    //     sys.getattr("path")?.call_method1("append", ("C:\\Users\\Aarav Maloo\\Desktop\\Student_Grading_System",))?;
    //
    //
    //
    //
    //     let interface = py.import("app.interface")?;
    //
    //
    //     let help_app_func = interface.getattr("print1")?;
    //
    //
    //     help_app_func.call0()?;
    //
    //     Ok(())
    // })
}
