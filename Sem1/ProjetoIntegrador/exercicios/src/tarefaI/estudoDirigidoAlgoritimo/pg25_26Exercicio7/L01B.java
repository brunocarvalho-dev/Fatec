package tarefaI.estudoDirigidoAlgoritimo.pg25_26Exercicio7;

// b)   Ler  uma  temperatura  em  graus  Fahrenheit  e
//      apresentá-la  convertida  em  graus  Celsius.
//      A  fórmula  de conversão é C ← (F - 32) * (5/9) ,
//      sendo F a temperatura em Fahrenheit e C a temperatura em Celsius.

import javax.swing.*;

public class L01B {
    public static void main() {
        double f, c;
        String result;

        c = Double.parseDouble(
                JOptionPane.showInputDialog(
                        "digite  temperatura em fahrenheit:").replace(",","."));

       f = conversionCelcius(c);
       result = String.format("O valor de "+String.format("%.2f",c) +" ºC"+
                       "\nem fahrenheit é: "+String.format("%.2f",f)+" F");

       System.out.println(result);
        JOptionPane.showMessageDialog(null,result);
    }
    public static double conversionCelcius(double fahrenheit) {
        double c = 0;
        c = Double.valueOf(((fahrenheit - 32)*9) / 5);
        return c;
    }
}
