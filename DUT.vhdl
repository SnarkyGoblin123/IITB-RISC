-- A DUT entity is used to wrap your design.
--  This example shows how you can do this for the
--  Full-adder.

library ieee;
use ieee.std_logic_1164.all;
entity DUT is
   port(input_vector: in std_logic_vector(0 downto 0);
       	output_vector: out std_logic_vector(129 downto 0));
end entity;

architecture DutWrap of DUT is
   component pipeline is
port (pc, r1, r2, r3, r4, r5, r6, r7 : out std_logic_vector(15 downto 0); 
	c_flag, z_flag: out std_logic;
	clock : in std_logic);
		end component;
begin

   -- A/output vector element ordering is critical,
   -- and must match the ordering in the trace file!
   add_instance: pipeline port map(pc => output_vector(15 downto 0),
		r1 => output_vector(31 downto 16),
		r2 => output_vector(47 downto 32),
		r3 => output_vector(63 downto 48),
		r4 => output_vector(79 downto 64),
		r5 => output_vector(95 downto 80),
		r6 => output_vector(111 downto 96),
		r7 => output_vector(127 downto 112),
		c_flag => output_vector(128),
		z_flag => output_vector(129),
		clock => input_vector(0));

end DutWrap;

