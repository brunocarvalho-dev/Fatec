package tarefaI.estudoDirigidoAlgoritimo.pg25_26Exercicio7;

import javax.swing.*;

/* d)   Efetuar  o  cálculo  da  quantidade  de  litros  de  combustível  gasta    em  uma  viagem,
        utilizando  um automóvel  que  faz  12  Km  por  litro.
      Para  obter  o  cálculo,  o  usuário  deve  fornecer:
      o  tempo  gasto (TEMPO);
      a velocidade  média (VELOCIDADE) durante  a viagem.
      Desta forma, será possível obter a distância  percorrida  com  a  fórmula:
      DISTANCIA ←  TEMPO  *  VELOCIDADE.  Possuindo  o  valor  da distância,
      basta  calcular  a  quantidade  de  litros  de  combustível  utilizada  na  viagem
      com  a  fórmula LITROS_USADOS ← DISTANCIA / 12.
      Ao final, o programa deve apresentar os valores da velocidade média  (VELOCIDADE),
      tempo  gasto  na  viagem  (TEMPO),  a  distancia  percorrida  (DISTANCIA)
      e  a quantidade de litros (LITROS_USADOS) utilizada na viagem
*/
public class L01D {
    static void main(String[] args) {
        double timeHour;
        String timeHourAndMinuts;
        double distance;
        double speed;
        double fuelConsumption;

        timeHour = Double.valueOf(JOptionPane.showInputDialog("Digite quantas horas de viagem: ").replace(",","."));
        speed = Double.valueOf(JOptionPane.showInputDialog("Digite a velocidade média do percurso: ").replace(",","."));

        timeHourAndMinuts = returMinutsAndHour(timeHour);

        distance = timeHour * speed;
        fuelConsumption = distance/12;
        
        JOptionPane.showMessageDialog(null, "De acordo com os dados fornecidos:"+
                        "\nA velocidade média: " + speed + "km/h" +
                        "\nO tempo  gasto  na  viagem: " + timeHourAndMinuts +"h"+
                        "\nA  distancia  percorrida: "+distance +"km"+
                        "\nA quantidade de combustivél consumido na viagem: " + fuelConsumption + "litros");

    }
    private static String returMinutsAndHour(Double hour){
        double minuts;
        String hourMinuts;
        int conversion = hour.intValue();
        minuts = hour - conversion;
        minuts = (minuts*60);
        hourMinuts = (String.format("%.0f",hour)+":"+String.format("%.0f",minuts));

        return hourMinuts;
    }

}
