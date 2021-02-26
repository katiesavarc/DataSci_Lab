import unittest
import nose.tools as nt
import numpy as np
import tools

class test_tools():

    def setUp(self):
        # Create a random array
        self.n = 4
        self.rand_array = np.random.normal(size=(self.n,self.n))

    def tearDown(self):
        pass

    def test_square(self):
        print(self.rand_array)

        # Test the square function to see if it
        # returns an array of the right size
        output_arr = tools.square(self.rand_array)
        nt.assert_equal(output_arr.shape, (self.n, self.n))

        # Test the square function to make sure that squaring
        # a matrix containing only 1s and 0s returns the same thing
        test_arr = np.diag(np.ones(self.n))
        output_arr = tools.square(test_arr)
        for i in range(self.n):
            for j in range(self.n):
                nt.assert_equal(output_arr[i,j], test_arr[i,j])

        # Test the square function for a known input/output
        test_arr = np.array([1, 2])
        output_arr = tools.square(test_arr)
        nt.assert_equal(output_arr[0], 1)
        nt.assert_equal(output_arr[1], 4)


    def test_get_pi(self):
        # See if the get_pi function really returns pi
        alleged_pi = tools.get_pi()
        nt.assert_almost_equal(alleged_pi, 3.141592653589)

    def test_picky(self):
        # Make sure that tools.picky raises an error if the
        # wrong type is inputted
        nt.assert_raises(TypeError, tools.picky, 'hey')
    
    def test_equal_length(self):
        ## test arrays are same length
        filename = "HT.dat"
        time, s, err = tools.load_dat(filename)
        len_time = len(time)
        len_s = len(s)
        len_err = len(err)
        nt.assert_equal(len_time, len_s, len_err)
    def test_tzero(self):
        ## test time at 0 is zero
        filename = "HT.dat"
        time, s, err = tools.load_dat(filename)
        t0 = time[0]
        nt.assert_equal(t0, 0)
    def test_nonzero_length(self):
        ## test array length > 0
        filename = "HT.dat"
        time, s, err = tools.load_dat(filename)
        lenZero_time = (len(time)==0)
        lenZero_s = (len(s)==0)
        lenZero_err = (len(err)==0)
        nt.assert_false(lenZero_s)
        nt.assert_false(lenZero_time)
        nt.assert_false(lenZero_err)


