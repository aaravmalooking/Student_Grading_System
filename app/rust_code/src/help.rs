pub fn help_app() {

    println!("It seems you want help with the app while the GUI is coming soon. \n");
    println!("When the symbol '$' appears, means you are in sudo mode, in simple words, you have full privileges on the database of your school... \n");
    println!("When the '>' symbol appears, the app asks for you to give input, which will then require you to use some flags and commands. (Will appear later in the help dialog) \n");
    println!("> flags: ");
    println!("Sudo mode flags: ");
    println!("/login");
    println!("the usrname and the pass ");
    println!("to create a new teacher, use /create_usr usrname, then you will be asked for usrpass, and to confirm it");
    println!("to modify teacher privileges, type: /usr_access their_class");
    println!("this is to ensure that only the class teacher or the root usr can modify the class not any other teacher");
    println!("and not any teacher to modify other than their own class");
    println!("/connect: connects to school database ");
    println!("/delete: deletes the whole school database or a class (for class user must be a class manager)");
    println!("/write: writes all changes from memory to the database");
    println!("Normal flags");
    println!("/select class: select a class");
    println!("/select section: select a section");
    println!("When in active section, use /select student_name for selecting and updating their marks");
    println!("When selected a active student, type /create term_name to create a new term");
    println!("When active is a term /create subject_name to create subject for them");
    println!("Create subject will create a row and the subject name in it");
    println!("While grading you will work with - flags which help you specify what you want to create in the report card");
    println!("/create -c: c stands for column, for example, /create -c marks && /create -c grade && /create -c remarks");
    println!("&& is the and operator.");
    println!("now to modify it type: /select -c column_name -subject_name");
    println!("now that subject and column is selected, modify it using: /modify 45 (in this case column is marks)");
    println!("to automate this process or any process:");
    println!("Ex_colmns = Marks, Remarks, Grade");
    println!("now example columns are made select all of them and use index (starts with 1)");
    println!("/select -c -a (-a for selected all columns) the indexes are automatically assigned ");
    println!("now to modify, use: /c1 (which is marks) 12 && /c2 good && /c3 A+ ");
    println!("to deselect type /deselect ");
    println!("to write the changes use /write");
    println!("to exit type /exit one by one it will exit everything");
    println!("to go to your class, or section again while in a active student selection, type /exit && /goto class_or_section_name");
    println!("/goto is used whenever you want to go to something discarding all changes made in the current selection");
    println!("To exit all modes and enter root, type su_root ");
    println!("To logout, type /logout (anywhere this command will work)");
    
}