/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */

/**
 *
 * @author Thaylon Guedes Santos
 */
public class FizzBuzz {

    public static String Verifica(int num) {
        int result3 = num % 3;
        int result5 = num % 5;

        return (result3 == 0) && (result5 == 0)?("FizzBuzz") : //VERIFICA MOD == 0
                (result3 == 0)?("Fizz") :// verifica mod de 3 == 0
                ((result5 == 0)?("Buzz") :// verifica mod de 5 == 0
                ("" + num));

    }

    public static void main(String[] args){
        System.out.println(0.1 + 0.2);
    }

}
