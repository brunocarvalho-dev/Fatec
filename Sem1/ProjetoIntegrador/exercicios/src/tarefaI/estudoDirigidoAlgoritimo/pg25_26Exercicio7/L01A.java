package tarefaI.estudoDirigidoAlgoritimo.pg25_26Exercicio7;

// a)    Ler  uma  temperatura  em  graus  Celsius  e,
//      apresentá-la  convertida  em  graus  Fahrenheit.
//      A  fórmula  de conversão é F ← (9 * C + 160) / 5,
//      sendo F a temperatura em Fahrenheit e C a temperatura em Celsius.

import javax.swing.*;

public class L01A {
    public static void main() {
    double f;
    double c;

    c = Double.valueOf(JOptionPane.showInputDialog("Digite a temperatura em Celcius: ").replace(",","."));
    f = (9 * c + 160) / 5;

    JOptionPane.showMessageDialog(null,
            "A temperatura de "+ String.format("%.1f",c) +"ºCelsius"+
            "\nequivale a "+ String.format("%.2f",f) +" Fahrenheit");


    }
    public static double conversionFahrenheit(double celcius){
        double f;
        f = (9 * celcius + 160) / 5;
        return f;
    } public static double conversionCelcius(double fahrenheit){
        double c;
        c = 5*fahrenheit/9 + 160;
        return c;
    }


}
