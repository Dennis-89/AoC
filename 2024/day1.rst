use std::{
    fs::File,
    io::{prelude::*, BufReader},
    path::Path,
};


fn read_lines(filepath: impl AsRef<Path>) -> Vec<String> {
    let file_content = File::open(filepath).expect("File not found");
    let buffer = BufReader::new(file_content);
    buffer.lines()
        .map(|l| l.expect("Can't read"))
        .collect()
}
fn main() {
    let lines = read_lines("/home/dennis/AoC/input.txt");

    println!("{}", counter);
}