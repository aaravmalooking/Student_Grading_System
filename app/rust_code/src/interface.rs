
use colored::*;
use std::*;
use crate::help;
use std::io::Write;


pub fn main() {


    loop {
        println!("Welcome To Grading, a better app for grades management ");
        println!("(Press h for help) (r to register) For security purposes, please enter your school admin password to access your data.");
        print!("{}", "$> ".purple().bold());
        io::stdout().flush().expect("Failed to flush stdout");


        let mut cmd = String::new();
        io::stdin().read_line(&mut cmd).expect("Failed to read input from iostream, try again");
        let cmd_ = cmd.trim().to_ascii_lowercase();


        if cmd_ == "h" {
            help::help_app();
            continue;

        }
        else if (cmd_ == "/login") {
            // TODO : call login func, from python and create the func in




        }
    }
}