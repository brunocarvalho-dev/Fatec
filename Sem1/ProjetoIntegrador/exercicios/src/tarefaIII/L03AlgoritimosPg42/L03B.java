package tarefaIII.L03AlgoritimosPg42;

import javax.swing.*;

/*
  b. Efetuar a leitura de um valor inteiro positivo ou negativo e apresentar o número lido como sendo um
  valor positivo, ou seja, o programa deverá apresentar o módulo de um número fornecido. Lembre-se
  de verificar se o número fornecido é menor que zero; sendo, multiplique-o por -1.
 */
public class L03B {
    static void main() {
        boolean valid = true;
        double number = 0;
        while (valid) {
            try {
                number = Math.abs(Double.valueOf(JOptionPane.showInputDialog("Digite um número inteiro positivo ou negativo: ")));
                valid = false;
            } catch (NumberFormatException e) {
                JOptionPane.showMessageDialog(null, "Entrada inválida. Por favor, digite um número inteiro.");
            }
        }
        System.out.println("O módulo do número fornecido é: " + number);
    }
}
