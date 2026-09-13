package tarefaI.estudoDirigidoAlgoritimo.pg25_26Exercicio7;

import javax.swing.*;

public class L01G {
    static void main() {
        double valA, valB, valC, valD, result;

        valA = Double.valueOf(JOptionPane.showInputDialog("Digite o valor de A:").replace(",", "."));
        valB = Double.valueOf(JOptionPane.showInputDialog("Digite o valor de B:").replace(",", "."));
        valC = Double.valueOf(JOptionPane.showInputDialog("Digite o valor de C:").replace(",", "."));
        valD = Double.valueOf(JOptionPane.showInputDialog("Digite o valor de D:").replace(",", "."));

        result = distributiva(valA, valB, valC, valD);

        JOptionPane.showMessageDialog(null, "O valor da distributiva de:"
                + "\nA: " + String.format("%.2f", valA) + ";"
                + "\nB: " + String.format("%.2f", valB) + ";"
                + "\nC: " + String.format("%.2f", valC) + ";"
                + "\nD: " + String.format("%.2f", valD) + ";"
                + "\nTotal: " + String.format("%.2f", result));
    }
    private static double distributiva(double valA, double valB, double valC, double valD) {
        double distributiva;
        distributiva = (valA * valB) + (valA * valC) + (valA * valD) + (valB * valC) + (valB * valD) + (valC * valD);
        return distributiva;
    }

}
