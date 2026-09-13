package tarefaI.estudoDirigidoAlgoritimo.pg25_26Exercicio7;
// f)    Ler dois valores (inteiros, reais ou caracteres) para as variáveis A e B,
// e efetuar a troca dos valores de forma que a variável A passe a possuir o valor da variável B,
// e a variável B passe a possuir o valor da variável A.
// Apresentar os valores trocados

import javax.swing.*;

public class L01F {
    static void main() {
        double firstValue;
        double secundValue;

        firstValue = Double.valueOf(JOptionPane.showInputDialog("Digite o valor de A: ").replace(",","."));
        secundValue = Double.valueOf(JOptionPane.showInputDialog("Digite o valor de B: ").replace(",","."));

        JOptionPane.showMessageDialog(null, "o valor de A: " + firstValue
                + "\no valor de B: " + secundValue);

        double trocador;
        trocador = firstValue;
        firstValue = secundValue;
        secundValue = trocador;

        JOptionPane.showMessageDialog(null, "Apos a troca:" +
                "\no valor de A: " + firstValue
                + "\no valor de B: " + secundValue);

    }

}
