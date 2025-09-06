use itertools::Itertools;
use std::fs::read_to_string;

fn is_safe(report: &[i32]) -> bool {
    let mut safe_up: bool = true;
    let mut safe_down: bool = true;
    for (x, y) in report.into_iter().tuple_windows() {
        safe_up &= 1 <= x - y && x - y <= 3;
        safe_down &= 1 <= y - x && y - x <= 3;
    }
    safe_up || safe_down
}

fn count_safe_reports(reports: &[Vec<i32>]) -> usize {
    reports.iter().filter(|report| is_safe(report)).count()
}

fn skip_index(iterable: &[i32], index: usize) -> Vec<i32> {
    iterable
        .into_iter()
        .enumerate()
        .filter(|&(i, _)| i != index)
        .map(|(_, &v)| v)
        .collect()
}

fn count_tolerated_safe_reports(reports: &[Vec<i32>]) -> usize {
    reports
        .iter()
        .filter(|report| {
            is_safe(report) || (0..report.len()).any(|index| is_safe(&skip_index(report, index)))
        })
        .count()
}

fn parse_lines<'a>(lines: impl Iterator<Item = &'a str>) -> Vec<Vec<i32>> {
    lines
        .map(|line| {
            line.split_whitespace()
                .map(|word| word.parse().unwrap())
                .collect()
        })
        .collect()
}

fn main() {
    let input =
        read_to_string("/home/dennis/PycharmProjects/AdventofCode/2024/Day02/input02.txt").unwrap();
    let reports = parse_lines(input.lines());
    println!("{:?}", count_safe_reports(&reports));
    println!("{:?}", count_tolerated_safe_reports(&reports));
}
