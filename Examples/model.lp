\ Model problemadoscombustiveis
\ LP format - for model browsing. Use MPS format to capture full model detail.
Minimize
 [ 20 Vol_n_atendido[0] * K[0,0] + 60 Vol_n_atendido[0] * K[0,1]
   + 16 Vol_n_atendido[1] * K[1,0] + 48 Vol_n_atendido[1] * K[1,1]
   + 12 Vol_n_atendido[2] * K[2,0] + 36 Vol_n_atendido[2] * K[2,1] ] / 2 
Subject To
 restricao_1[0]: Bin_tipo[0,0] + Bin_tipo[0,1] + Bin_tipo[0,2] = 1
 restricao_1[1]: Bin_tipo[1,0] + Bin_tipo[1,1] + Bin_tipo[1,2] = 1
 restricao_1[2]: Bin_tipo[2,0] + Bin_tipo[2,1] + Bin_tipo[2,2] = 1
 restricao_1[3]: Bin_tipo[3,0] + Bin_tipo[3,1] + Bin_tipo[3,2] = 1
 restricao_1[4]: Bin_tipo[4,0] + Bin_tipo[4,1] + Bin_tipo[4,2] = 1
 restricao_4[0]: Vol_n_atendido[0] <= 500
 restricao_4[1]: Vol_n_atendido[1] <= 500
 restricao_4[2]: Vol_n_atendido[2] <= 500
 restricao_5[0]: Vol[0] + Vol_n_atendido[0] = 2900
 restricao_5[1]: Vol[1] + Vol_n_atendido[1] = 4000
 restricao_5[2]: Vol[2] + Vol_n_atendido[2] = 4900
 restricao_8[0]: K[0,0] + K[0,1] = 1
 restricao_8[1]: K[1,0] + K[1,1] = 1
 restricao_8[2]: K[2,0] + K[2,1] = 1
 restricao_2[0]: Vol[0] + [ - Bin_tipo[0,0] * Vol[0,0]
   - Bin_tipo[1,0] * Vol[1,0] - Bin_tipo[2,0] * Vol[2,0]
   - Bin_tipo[3,0] * Vol[3,0] - Bin_tipo[4,0] * Vol[4,0] ] = 0
 restricao_2[1]: Vol[1] + [ - Bin_tipo[0,1] * Vol[0,1]
   - Bin_tipo[1,1] * Vol[1,1] - Bin_tipo[2,1] * Vol[2,1]
   - Bin_tipo[3,1] * Vol[3,1] - Bin_tipo[4,1] * Vol[4,1] ] = 0
 restricao_2[2]: Vol[2] + [ - Bin_tipo[0,2] * Vol[0,2]
   - Bin_tipo[1,2] * Vol[1,2] - Bin_tipo[2,2] * Vol[2,2]
   - Bin_tipo[3,2] * Vol[3,2] - Bin_tipo[4,2] * Vol[4,2] ] = 0
 restricao_3[0]: [ Bin_tipo[0,0] * Vol[0,0] + Bin_tipo[0,1] * Vol[0,1]
   + Bin_tipo[0,2] * Vol[0,2] ] <= 2700
 restricao_3[1]: [ Bin_tipo[1,0] * Vol[1,0] + Bin_tipo[1,1] * Vol[1,1]
   + Bin_tipo[1,2] * Vol[1,2] ] <= 2800
 restricao_3[2]: [ Bin_tipo[2,0] * Vol[2,0] + Bin_tipo[2,1] * Vol[2,1]
   + Bin_tipo[2,2] * Vol[2,2] ] <= 1100
 restricao_3[3]: [ Bin_tipo[3,0] * Vol[3,0] + Bin_tipo[3,1] * Vol[3,1]
   + Bin_tipo[3,2] * Vol[3,2] ] <= 1800
 restricao_3[4]: [ Bin_tipo[4,0] * Vol[4,0] + Bin_tipo[4,1] * Vol[4,1]
   + Bin_tipo[4,2] * Vol[4,2] ] <= 3400
 restricao_6[0]: [ Vol_n_atendido[0] * K[0,0] - Vol_n_atendido[0] * K[0,1]
   ] <= 100
 restricao_6[1]: [ Vol_n_atendido[1] * K[1,0] - Vol_n_atendido[1] * K[1,1]
   ] <= 100
 restricao_6[2]: [ Vol_n_atendido[2] * K[2,0] - Vol_n_atendido[2] * K[2,1]
   ] <= 100
 restricao_7[0]: [ Vol_n_atendido[0] * K[0,0] + Vol_n_atendido[0] * K[0,1]
   ] >= 100
 restricao_7[1]: [ Vol_n_atendido[1] * K[1,0] + Vol_n_atendido[1] * K[1,1]
   ] >= 100
 restricao_7[2]: [ Vol_n_atendido[2] * K[2,0] + Vol_n_atendido[2] * K[2,1]
   ] >= 100
Bounds
Binaries
 Bin_tipo[0,0] Bin_tipo[0,1] Bin_tipo[0,2] Bin_tipo[1,0] Bin_tipo[1,1]
 Bin_tipo[1,2] Bin_tipo[2,0] Bin_tipo[2,1] Bin_tipo[2,2] Bin_tipo[3,0]
 Bin_tipo[3,1] Bin_tipo[3,2] Bin_tipo[4,0] Bin_tipo[4,1] Bin_tipo[4,2]
 K[0,0] K[0,1] K[1,0] K[1,1] K[2,0] K[2,1]
Generals
 Vol[0,0] Vol[0,1] Vol[0,2] Vol[1,0] Vol[1,1] Vol[1,2] Vol[2,0] Vol[2,1]
 Vol[2,2] Vol[3,0] Vol[3,1] Vol[3,2] Vol[4,0] Vol[4,1] Vol[4,2] Vol[0]
 Vol[1] Vol[2] Vol_n_atendido[0] Vol_n_atendido[1] Vol_n_atendido[2]
End
