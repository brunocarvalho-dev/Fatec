// e)Efetuar o cálculo e a apresentação do valor de uma prestação em atraso,
// utilizando a fórmula PRESTACAO ← VALOR + (VALOR * TAXA/100) * TEMPO).

package tarefaI.estudoDirigidoAlgoritimo.pg25_26Exercicio7;

import javax.swing.*;

public class L01E {
    static void main() {
    double installmentAmount;
    double interest;
    double valueTotal;
    int days;

     installmentAmount = Double.parseDouble(JOptionPane.showInputDialog("Digite o valor da prestação: ").replace(",","."));
     interest = Double.parseDouble(JOptionPane.showInputDialog("Digite taxa de juros: ").replace(",","."));
     days = Integer.parseInt(JOptionPane.showInputDialog("Digite quantos dias de atraso: "));

     valueTotal = simpleInterest(interest,installmentAmount,days)+installmentAmount;

     JOptionPane.showMessageDialog(null, "O valor total da prestação com juros é R$: "+ String.format("%.2f",valueTotal));

    }

    private static double simpleInterest(double interestRate, double valueAsset, int mouts) {
        double interestAmount;
        interestAmount = valueAsset * (interestRate / 100)* mouts;
        return interestAmount;
    }
}
