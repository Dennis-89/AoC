use std::{
    fs::File, io::{prelude::*, BufReader}, path::Path
};
extern crate itertools;
use itertools::Itertools;


fn is_safe(report: Vec<i32>) -> bool {
    let mut safe_up: Vec<bool> = Vec::new();
    let mut safe_down: Vec<bool> = Vec::new();
    for (x, y) in report.into_iter().tuple_windows() {
        if 1 <= x - y && x -y <= 3 {
            safe_up.push(true);
        } else {safe_up.push(false)}
        if 1 <= y - x && y - x <= 3 {
            safe_down.push(true);
        } else {safe_down.push(false)}
    };
    safe_up.iter().all(|x| *x) || safe_down.iter().all(|x| *x)
}


fn get_safe_reports(reports: Vec<Vec<i32>>) -> u16 {
    let safe_reports: Vec<_>= reports.into_iter()
        .map(|report| is_safe(report))
        .collect();
    safe_reports.into_iter().filter(|b| *b).count().try_into().unwrap()
}


fn skip_index(iterable: Vec<i32>, index: usize) -> Vec<i32> {
    iterable.into_iter()
        .enumerate()
        .filter(|&(i, _)| i != index)
        .map(|(_, v)| v)
        .collect()
}


fn get_tolerated_safe_reports(reports: Vec<Vec<i32>>) -> u16 {
    let mut safe_reports: u16 = 0;
    for report in reports {
        let mut safe = 0;
        if is_safe(report.clone()) == true {
            safe = 1;
        } else {
            for index in 0..report.len() {
                let optimized_report = skip_index(report.clone(), index);
                if is_safe(optimized_report) == true {
                    safe = 1;
                    break;
                };
            };
        };
        safe_reports += safe;
        };
    safe_reports
    }


fn read_lines(filepath: impl AsRef<Path>) -> Vec<String> {
    let file_content = File::open(filepath).expect("File not found");
    let buffer = BufReader::new(file_content);
    buffer.lines()
        .map(|l| l.expect("Can't read"))
        .collect()
}


fn format_input(lines: Vec<String>) -> Vec<Vec<i32>> {
    let mut reports: Vec<Vec<_>> = Vec::new();
    for line in lines {
        let line = line.split_whitespace().map(|x| x.parse().unwrap()).collect();
        reports.push(line);
    };
    reports

}


fn main() {
    let lines = read_lines("/home/dennis/PycharmProjects/AdventofCode/2024/Day02/input02.txt");
    let reports = format_input(lines);
    println!("{:?}", get_safe_reports(reports.clone()));
    println!("{:?}", get_tolerated_safe_reports(reports));
}


