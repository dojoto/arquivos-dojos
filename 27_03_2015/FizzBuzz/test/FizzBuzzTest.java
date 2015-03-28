/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */

import org.junit.After;
import org.junit.Before;
import org.junit.Test;
import static org.junit.Assert.*;

/**
 *
 * @author Thaylon Guedes Santos
 */
public class FizzBuzzTest {

    public FizzBuzzTest() {
    }

    @Before
    public void setUp() {
    }

    @After
    public void tearDown() {
    }

    /**
     * Test of Verifica method, of class FizzBuzz.
     */
    @Test
    public void testVerifica3() {
        for (int i = 1; i <= 100; i++) {
            if (i % 3 == 0 && i % 5 != 0) {
                assertEquals("Fizz", FizzBuzz.Verifica(i));
            }
        }
    }

    @Test
    public void testVerifica5() {
        for (int i = 1; i <= 100; i++) {
            if (i % 5 == 0 && i % 3 != 0) {
                assertEquals("Buzz", FizzBuzz.Verifica(i));
            }
        }
    }

    @Test
    public void testVerifica3e5() {
        for (int i = 1; i <= 100; i++) {
            if (i % 5 == 0 && i % 3 == 0) {
                assertEquals("FizzBuzz", FizzBuzz.Verifica(i));
            }
        }
    }

    @Test
    public void testVerificaNaoE(){
        for (int i = 1; i <= 100; i++) {
            if (i % 5 != 0 && i % 3 != 0) {
                assertEquals(""+i, FizzBuzz.Verifica(i));
            }
        }
    }

}
