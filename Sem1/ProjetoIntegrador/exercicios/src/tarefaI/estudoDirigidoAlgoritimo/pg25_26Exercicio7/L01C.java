package tarefaI.estudoDirigidoAlgoritimo.pg25_26Exercicio7;
// c) Calcular e apresentar o valor do volume de uma lata de óleo,
//   utilizando a fórmula:AlturaRaioVolume**2π←

import javax.swing.*;

public class L01C {
    static void main() {
        int ask;
        String texto = "";
        String result = null;
        double radius;
        double height;

        do {

            texto = (JOptionPane.showInputDialog("Digite: \n" +
                    "\n1 - para  calcular área da superfície lateral do cilindro: " +
                    "\n2 - para  calcular área superficial total do cilindro: " +
                    "\n3 - para  calcular Volume do cilindro: " +
                    "\n4 - para  calcular área da base do cilindro: " +
                    "\n0 - para  sair. "));


            ask = Integer.parseInt(String.valueOf(texto.charAt(0)));

            switch (ask) {
                case 1: {
                    radius = valueRadius();
                    height = valueHeight();
                    result = lateralSurfaceAreaCylinder(radius, height);
                    break;
                }
                case 2: {
                    radius = valueRadius();
                    height = valueHeight();
                    result = totalSurfaceAreaCylinder(radius, height);
                    break;
                }
                case 3: {
                    radius = valueRadius();
                    height = valueHeight();
                    result = volumeCylinder(radius, height);
                    break;
                }
                case 4: {
                    radius = valueRadius();
                    result = baseAreaCylinder(radius);
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
            JOptionPane.showMessageDialog(null,
                    result );
        }while (ask != 0);

    }
    public static double valueRadius(){

        double radius = Double.parseDouble(JOptionPane.showInputDialog("Digite o valor do raio do cilindro: ").replace(",","."));

        return radius;
    }
    public static double valueHeight(){
         double height = Double.parseDouble(JOptionPane.showInputDialog("Digite o valor da altura do cilindro: ").replace(",","."));

         return height;
    }

    public static String lateralSurfaceAreaCylinder(double radius, double height) {

        String result = "A àrea da lateral do cilindro é: "+String.format("%.2f", (2 * Math.PI * radius) * height)+"cm²";

        return result;
    }

    public static String totalSurfaceAreaCylinder(double radius, double height) {

        String result = "A àrea total do cilindro é: " + String.format("%.2f",Math.PI * radius * (radius + height)*2) + "cm²";

        return result;

    }

    public static String volumeCylinder(double radius, double height) {

        String result = "O volume total do cilindro é: "+String.format("%.2f",(2 * Math.PI * radius) * height)+"cm³";

        return result;
    }

    public static String baseAreaCylinder(double radius) {


        String result = "A àrea da base do cilindro é: "+String.format("%.2f",Math.pow(radius,2)*Math.PI)+"cm²";

        return result;
    }
}