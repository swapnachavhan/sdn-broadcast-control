from pox.core import core
import pox.openflow.libopenflow_01 as of

log = core.getLogger()

class BroadcastControl(object):
    def __init__(self, connection):
        self.connection = connection
        connection.addListeners(self)

    def _handle_PacketIn(self, event):
        packet = event.parsed

        #  1. Allow ARP packets (VERY IMPORTANT)
        if packet.type == 0x0806:
            msg = of.ofp_packet_out()
            msg.data = event.ofp
            msg.actions.append(of.ofp_action_output(port=of.OFPP_FLOOD))
            self.connection.send(msg)
            return

        #  2. Block other broadcast/multicast packets
        if packet.dst.is_multicast:
            log.info("Blocking broadcast packet")
            return

        # 3. Allow normal unicast traffic
        msg = of.ofp_packet_out()
        msg.data = event.ofp
        msg.actions.append(of.ofp_action_output(port=of.OFPP_FLOOD))
        self.connection.send(msg)


def launch():
    def start_switch(event):
        log.info("Switch connected")
        BroadcastControl(event.connection)

    core.openflow.addListenerByName("ConnectionUp", start_switch)
