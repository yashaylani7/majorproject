import os
import shutil
from Frontend.src.Document_Formatter import *
from Backend.Database.lesson_db import lesson_data as ld
from Backend.Database.lesson_assigning_db import lesson_assiging_data as lad
from Backend.Database.student_db import student_data as sd
from Frontend.Teacher_UI import ui_assign_lesson
import datetime


class Lesson_Assigning_Window(QMainWindow):  # Home extends QMainWindow

    def __init__(self, ui_object):
        super(QMainWindow, self).__init__()

        # window
        self.lesson_assinging_window = ui_object
        self.form = None
        self.table_data = None
        self.rows = None
        self.columns = None

        # table property
        self.lesson_assinging_window.lsn_table_assigning_lessons.setEditTriggers(QAbstractItemView.NoEditTriggers)

        self.populate_student_list()
        self.populate_lesson_assigning_table()

    def populate_student_list(self):

        # clear the list before populating
        self.lesson_assinging_window.lsn_list_students.clear()

        student_details = sd().load_table()
        data = [(x[0], x[1]) for x in student_details]

        self.lesson_assinging_window.lsn_list_students.addItems(
            [str(x[0]) + '. ' + x[1] for x in data])
        print(data)

    def populate_lesson_assigning_table(self):

        # clear previous data before populating
        self.lesson_assinging_window.lsn_table_assigning_lessons.clearContents()
        self.lesson_assinging_window.lsn_table_assigning_lessons.setRowCount(0)

        self.table_data = lad().load_table()
        self.rows = len(self.table_data)
        self.columns = self.lesson_assinging_window.lsn_table_assigning_lessons.columnCount()
        print(self.rows, self.columns, self.table_data)

        for row in range(self.rows):
            self.lesson_assinging_window.lsn_table_assigning_lessons.insertRow(row)
            for col in range(self.columns):
                print(row, col, self.table_data[row][col])
                self.lesson_assinging_window.lsn_table_assigning_lessons.setItem(row, col, QTableWidgetItem(
                    str(self.table_data[row][col])))

    def assign_lesson(self):

        lad().create_table()

        # get the selected student name and id
        model = self.lesson_assinging_window.lsn_list_students.model()
        index = self.lesson_assinging_window.lsn_list_students.currentIndex()
        print(model.data(index))

        # show warning if student name is not selected
        if model.data(index) is None:
            show_warning_message(
                "Warning", "Please select a student from the list on the left and then press the button")
            return

        std_id, std_name = model.data(index).split('. ')

        # load & set up the Student Add Info page [must use self.custom_widget else it will be destroyed as soon as the function ends]
        self.custom_widget = QWidget()
        self.form = ui_assign_lesson.Ui_Form()
        self.form.setupUi(self.custom_widget)
        self.custom_widget.setWindowModality(Qt.ApplicationModal)
        self.custom_widget.show()

        self.form.lsn_cmb_lesson_list.clear()

        # set window icon and title
        self.custom_widget.setWindowIcon(
            QIcon("../Teacher/Frontend/Images/primary_logo.png"))
        self.custom_widget.setWindowTitle("Assign Lesson")

        # set the student name and id in the form
        self.form.lsn_edit_student_id.setText(std_id)
        self.form.lsn_edit_student_name.setText(std_name)

        # disable first option
        self.form.lsn_cmb_mcq_list.model().item(0).setEnabled(False)
        self.form.lsn_cmb_sequence_list.model().item(0).setEnabled(False)
        self.form.lsn_cmb_matching_list.model().item(0).setEnabled(False)
        self.form.lsn_cmb_puzzle_list.model().item(0).setEnabled(False)

        # get lesson data from table
        lesson_details = ld().load_table()
        print("Details: ", lesson_details)
        data = [str(x[1]).split('/')[-1] for x in lesson_details]
        self.form.lsn_cmb_lesson_list.addItems(data)

        # get Matching id
        matching_folder = 'Lessons\\Matching_Images'
        matching_folder_files = os.listdir(matching_folder)
        matching_folder_names = [x[2:] for x in matching_folder_files]
        print("Matching Folder Files: ", matching_folder_names)
        self.form.lsn_cmb_matching_list.addItems(matching_folder_names)

        # get MCQ id
        mcq_folder = 'Lessons\\MCQ_Questions'
        mcq_folder_files = os.listdir(mcq_folder)
        mcq_folder_names = [x[2:] for x in mcq_folder_files]
        print("MCQ Folder Files: ", mcq_folder_names)
        self.form.lsn_cmb_mcq_list.addItems(mcq_folder_names)

        # get Puzzle id
        puzzle_folder = 'Lessons\\Puzzle_Images'
        puzzle_folder_files = os.listdir(puzzle_folder)
        puzzle_folder_names = [x[2:] for x in puzzle_folder_files]
        print("Puzzle Folder Files: ", puzzle_folder_names)
        self.form.lsn_cmb_puzzle_list.addItems(puzzle_folder_names)

        # get Sequence Id
        sequence_folder = 'Lessons\\Sequence_Images'
        sequence_folder_files = os.listdir(sequence_folder)
        sequence_folder_names = [x[2:] for x in sequence_folder_files]
        print("Sequence Folder Files: ", sequence_folder_names)
        self.form.lsn_cmb_sequence_list.addItems(sequence_folder_names)

        # connect the buttons
        self.form.lsn_btn_assign_lsn_to_std.clicked.connect(self.done_assigning_lesson)

    def done_assigning_lesson(self):

        # get data from the form
        get_lesson_id = self.form.lsn_cmb_lesson_list.currentText()
        print("ID: ", get_lesson_id)

        get_mcq_id = self.form.lsn_cmb_mcq_list.currentText()
        print("MCQ ID: ", get_mcq_id)

        get_sequence_id = self.form.lsn_cmb_sequence_list.currentText()
        print("Sequence ID: ", get_sequence_id)

        get_matching_id = self.form.lsn_cmb_matching_list.currentText()
        print("Matching ID: ", get_matching_id)

        get_puzzle_id = self.form.lsn_cmb_puzzle_list.currentText()
        print("Puzzle ID: ", get_puzzle_id)

        if get_lesson_id == '':
            show_warning_message("Select Lesson", "Please select a lesson!")
            return

        warning = show_confirmation_message("Confirmation", "Are you sure you want to assign the lesson?")

        if warning:

            get_student_id = self.form.lsn_edit_student_id.text()
            get_student_name = self.form.lsn_edit_student_name.text()
            assigning_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            data = [get_student_id, get_student_name, get_lesson_id, get_mcq_id, get_sequence_id, get_matching_id,
                    get_puzzle_id, assigning_time]

            # insert data into the table
            lad().add_entry(data)

            # hide the form
            self.custom_widget.hide()

            # get the details of lesson assigning table
            rows = self.lesson_assinging_window.lsn_table_assigning_lessons.rowCount()
            columns = self.lesson_assinging_window.lsn_table_assigning_lessons.columnCount()

            # add new row
            self.lesson_assinging_window.lsn_table_assigning_lessons.insertRow(rows)

            for col in range(columns):
                print(col, ' ', data[col])
                self.lesson_assinging_window.lsn_table_assigning_lessons.setItem(
                    rows, col, QTableWidgetItem(str(data[col])))

            # Copy the selected folders to the content folder
            copy_folder_name = 'Student_Content\\' + get_student_id + '_' + get_lesson_id

            lesson_folder = r'Lessons\\Lessons\\' + get_lesson_id
            mcq_folder = r'Lessons\\MCQ_Questions\\q_' + get_mcq_id
            puzzle_folder = r'Lessons\\Puzzle_Images\\p_' + get_puzzle_id
            sequence_folder = r'Lessons\\Sequence_Images\\s_' + get_sequence_id
            matching_folder = r'Lessons\\Matching_Images\\m_' + get_matching_id

            # Create the 'Student_Content' folder if it doesn't exist
            os.makedirs('Student_Content', exist_ok=True)

            # Remove the existing destination folder if it exists
            if os.path.exists(copy_folder_name):
                shutil.rmtree(copy_folder_name)

            # Copy the lesson folder
            lesson_folder = r'Lessons\\Lessons\\' + get_lesson_id
            shutil.copytree(lesson_folder, copy_folder_name + '\\' + get_lesson_id)

            # Copy the other folders
            shutil.copytree(mcq_folder, copy_folder_name + '\\q_' + get_mcq_id)
            shutil.copytree(puzzle_folder, copy_folder_name + '\\p_' + get_puzzle_id)
            shutil.copytree(sequence_folder, copy_folder_name + '\\s_' + get_sequence_id)
            shutil.copytree(matching_folder, copy_folder_name + '\\m_' + get_matching_id)

            os.startfile('Student_Content')

        else:

            print("Warning false!!")
