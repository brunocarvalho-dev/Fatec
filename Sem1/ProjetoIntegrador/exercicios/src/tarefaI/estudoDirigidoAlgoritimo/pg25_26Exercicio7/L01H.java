// h)    Elaborar um programa que calcule e apresente o volume de uma caixa retangular,
// por meio da fórmula VOLUME ← COMPRIMENTO * LARGURA * ALTURA.
package tarefaI.estudoDirigidoAlgoritimo.pg25_26Exercicio7;

import javax.swing.*;

public class L01H {
    static void main() {
        //tradução resultado, comprimento, altura, largura;

        boxCalculation();

    }

    private static double areaDaBaseCaixa(double length, double width) {
        double area;
        area = length * width;
        return area;
    }

    private static double areaDaCaixa(double length, double width, double height) {
        double area;
        area = ((width * height) * 2) + ((width * length) * 2) + ((length * height) * 2);
        return area;
    }

    private static double volumeDaCaixa(double length, double width, double height) {
        double volume;
        volume = length * width * height;
        return volume;
    }

    private static String askOperation() {
        String response = (JOptionPane.showInputDialog("Digite: \n" +
                "\n1 - para  calcular área superficial total do cubo: " +
                "\n2 - para  calcular Volume do cubo: " +
                "\n3 - para  calcular área da base do cubo: " +
                "\n0 - para  sair. "));

        return response;
    }

    private static void boxCalculation() {
        double length, width, height, result;
        String resultText, texto;
        int ask;

        do {

            texto = askOperation();
            try {
                ask = Integer.parseInt(String.valueOf(texto.charAt(0)));
            } catch (NumberFormatException e) {
                ask = -1;
            }

            switch (ask) {

                case 1: {
                    length = Double.parseDouble(JOptionPane.showInputDialog("Digite o valor do comprimento: ").replace(",", "."));
                    height = Double.parseDouble(JOptionPane.showInputDialog("Digite o valor da altura: ").replace(",", "."));
                    width = Double.parseDouble(JOptionPane.showInputDialog("Digite o valor da largura: ").replace(",", "."));

                    result = (areaDaCaixa(length, width, height));
                    resultText = "A àrea da caixa é : " + String.format("%.2f", result);
                    break;
                }
                case 2: {
                    length = Double.parseDouble(JOptionPane.showInputDialog("Digite o valor do comprimento: ").replace(",", "."));
                    height = Double.parseDouble(JOptionPane.showInputDialog("Digite o valor da altura: ").replace(",", "."));
                    width = Double.parseDouble(JOptionPane.showInputDialog("Digite o valor da largura: ").replace(",", "."));


                    result = (volumeDaCaixa(length, width, height));
                    resultText = "O volume da caixa é : " + String.format("%.2f", result);
                    break;
                }
                case 3: {
                    length = Double.parseDouble(JOptionPane.showInputDialog("Digite o valor do comprimento: ").replace(",", "."));
                    height = Double.parseDouble(JOptionPane.showInputDialog("Digite o valor da altura: ").replace(",", "."));
                    width = Double.parseDouble(JOptionPane.showInputDialog("Digite o valor da largura: ").replace(",", "."));


                    result = (areaDaBaseCaixa(length, width));
                    resultText = "A àrea da base da caixa é : " + String.format("%.2f", result);
                    break;
                }
                case 0: {
                    resultText = "Obrigado por sua interação! :)";
                    result = 0;
                    break;
                }
                default: {
                    resultText = "Valor inválido, digite novamente";
                    result = -1;
                    break;
                }
            }
            JOptionPane.showMessageDialog(null, resultText);
            System.out.println(result);
        } while (result != 0);

    }
}


