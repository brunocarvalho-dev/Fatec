package tarefaII.avaliacaoContinua;

import util.validationDouble;

import javax.swing.*;

public class L02D {
    public static void main() {
        int ask = -1;
        String result;
        String texto = JOptionPane.showInputDialog("Digite uma opção: \n"
                + "\n1 - Raio com diâmetro"
                + "\n2 - Área com raio"
                + "\n3 - Diametro com perimetro"
                + "\n4- Área com diâmetro"
                + "\n0 - Para sair");

        ask = Integer.parseInt(String.valueOf(texto.charAt(0)));
        do{
            switch (ask) {
                case 1: {
                    result = valueRadius_diameter();
                    break;
                }
                case 2: {
                    result = valueAreaCalc_radius();
                    break;
                }
                case 3: {

                    result = valueDiameter_perimeter();
                    break;
                }
                case 4: {
                    result = valueAreaCalc_diameter();
                    break;
                }
                case 0: {
                    result = "Obrigado por sua interação! :)";
                    break;
                }
                default: {
                    result = "Valor inválido, digite novamente";
                    break;
                }
            }
        } while (ask != 0);
        JOptionPane.showMessageDialog(null, result);
    }


    public static String valueDiameter_perimeter() {
        validationDouble valid = new validationDouble("Digite o valor do perimetro : ");
        String result = "O raio de acordo com o diametro é: " + String.format("%.2f", Math.PI * valid.getValor() / 2) + "cm²";

        return result;
    }

    public static String valueRadius_diameter() {

        String result = "O raio de acordo com o diametro é: " + String.format("%.2f", valueRadius_diameter_calc() / 2) + "cm²";

        return result;
    }

    private static double valueRadius_diameter_calc() {
        validationDouble valid = new validationDouble("Digite o valor do diametro : ");
        return valid.getValor();
    }

    public static String valueAreaCalc_diameter() {

        String result = "A Area total é: " + String.format("%.2f", Math.PI * Math.pow(valueRadius_diameter_calc(), 2)) + "cm²";

        return result;

    }

    public static String valueAreaCalc_radius() {

        String result = "A àrea total é: " + String.format("%.2f", Math.PI * Math.pow(valueRadius(), 2) + "cm²");

        return result;
    }

    private static double valueRadius() {
        validationDouble valid = new validationDouble("Digite o valor do raio : ");
        return valid.getValor();
    }

}