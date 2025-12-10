function printStudents(students) {
    console.log("Student List:");
    for (let name of students) {
        console.log(name);
    }
}

// Test data
const studentNames = ["Alice", "Bob", "Charlie"];
printStudents(studentNames);