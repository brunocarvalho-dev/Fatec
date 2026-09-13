package tarefaIII.L03AlgoritimosPg42;

import javax.swing.*;

/*
a. Ler dois valores numéricos inteiros e
apresentar o resultado da diferença do maior pelo menor valor.
*/
public class L03A {
    static void main() {
        double value1 = 0, value2 = 0, total;
        boolean validation = true;

        while (validation) {
            try {
                value1 = Double.valueOf(JOptionPane.showInputDialog("\nDigite o valor do primeiro termo: ").replace(",", "."));
                while (validation) {
                    try {
                        value2 = Double.valueOf(JOptionPane.showInputDialog("\nDigite o valor do segundo termo: ").replace(",", "."));
                        validation = false;
                    } catch (NumberFormatException e) {
                        JOptionPane.showMessageDialog(null, "\nValor do segundo termo inválido!, digite novamente");
                    }
                }
            } catch (NumberFormatException e) {
                JOptionPane.showMessageDialog(null, "\nValor do primeiro termo inválido!, digite novamente");
            }

        }
        total = highestValue(value1, value2);
        JOptionPane.showMessageDialog(null, "\n\nA diferença entre " + String.format("%.2f", value1)
                + " e " + String.format("%.2f", value2)+" é " + String.format("%.2f", total));
    }

    public static double highestValue(double valor1, double valor2) {
        double result;
        if (valor1 > valor2) {
            result = valor1 - valor2;
        } else {
            result = valor2 - valor1;
        }
        return result;
    }
}