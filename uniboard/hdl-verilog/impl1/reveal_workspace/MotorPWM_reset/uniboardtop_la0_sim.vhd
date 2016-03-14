-- =============================================================================
--  VHDL simulation model generated by IPExpress    01/10/2016    00:10:39         
--  Filename: uniboardtop_la0_sim.vhd                                          
--  Copyright(c) 2006 Lattice Semiconductor Corporation. All rights reserved.   
-- =============================================================================

-- WARNING - Changes to this file should be performed by re-running IPexpress
-- or modifying the .LPC file and regenerating the core.  Other changes may lead
-- to inconsistent simulation and/or implemenation results */

library IEEE; use IEEE.std_logic_1164.all; use IEEE.numeric_std.all;

entity uniboardtop_la0 is
    PORT (
        clk:		IN std_logic;
        reset_n:	IN std_logic;
        jtck:		IN std_logic;
        jrstn:		IN std_logic;
        jce2:		IN std_logic;
        jtdi:		IN std_logic;
        er2_tdo:	BUFFER std_logic;
        jshift:		IN std_logic;
        jupdate:	IN std_logic;
        trigger_din_0:	IN std_logic_vector (0 downto 0);
        trace_din:	IN std_logic_vector (16 downto 0);
        trigger_en:	IN std_logic;
        ip_enable:	IN std_logic
    );

end uniboardtop_la0;

architecture uniboardtop_la0_u of uniboardtop_la0 is
begin

    er2_tdo <= '0';

end uniboardtop_la0_u;
