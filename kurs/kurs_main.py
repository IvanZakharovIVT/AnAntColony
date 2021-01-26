from Ant import Ant, generateTests

if __name__ == "__main__":

    N1 = [
        {1:0, 5:0}, # S0
        {2:0, 4:0}, # S1
        {2:0, 3:0, 4:0}, # S2
        {1:0}, # S3
        {2:0, 4:0}, # S4
        {6:0}, # S5
        {2:0, 5:0, 6:0, 7:0}, # S6
        {7:0, 8:0}, # S7
        {9:0}, # S8
        {10:0}, # S9
        {}, # S10
    ]

    N2 = [
        {1:0, 5:0}, # S0
        {2:0, 4:0}, #1 Enrollment
        {3:0}, #2 Proposed
        {4:0}, #3 Scheduled
        {4:0, 5:0, 6:0}, #4 Open For Enrolment
        {4:0, 5:0, 6:0}, #5 Full
        {7:0}, #6 Close to Enrolment
        {7:0, 8:0, 9:0}, #7 Begining Taught
        {9:0}, #8 Final Exams
        {}, # S9
    ]

    N3 = [
        {1:0}, # S0
        {2:0}, #1 OFF
        {1:0, 3:0, 6:0}, #2 ON
        {2:0, 4:0, 5:0}, #3 21 Coffee
        {3:0, 5:0}, #4 211 Idle
        {3:0, 4:0}, #5 212 Busy
        {2:0, 7:0, 8:0}, #6 22 Cocoa
        {6:0, 8:0}, #7 221 Stop
        {6:0, 7:0}, #8 222 Streem
    ]

    print (generateTests(N1))

    print (N1)