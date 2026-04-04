**Organizing case list**

I need to create a detailed list of 100+ cases, but I want to keep it concise. I’m thinking of structuring it by category, with numbered IDs and brief steps or expectations. 100+ cases is a lot, but I can manage. I’ll aim for 10-15 cases per section, spread across about 10 sections. I’ll keep the format simple, using table-like bullets, but I’ll avoid overcomplicating it with too many headings. Let’s get started!
Here we go—this is a **concrete, review‑ready catalog of 100+ BLE test cases**, grouped by area, with IDs, intent, and core steps. You can drop this straight into a test management tool and then expand steps/expected results per your org’s template.

---

## 1. RF PHY test cases (TX/RX, coexistence)

**RF‑TX‑01:** TX power at nominal  
- **Goal:** Verify TX power matches spec at default setting.  
- **Steps:** Configure DUT to continuous TX on mid‑channel → Measure output power.  
- **Expected:** Within configured tolerance (e.g., ±2 dB).

**RF‑TX‑02:** TX power at min setting  
**RF‑TX‑03:** TX power at max setting  
**RF‑TX‑04:** TX power vs channel (low/mid/high)  
**RF‑TX‑05:** Frequency error at 1M PHY  
**RF‑TX‑06:** Frequency error at 2M PHY  
**RF‑TX‑07:** Frequency error at Coded PHY  
**RF‑TX‑08:** Modulation index at 1M  
**RF‑TX‑09:** Modulation index at 2M  
**RF‑TX‑10:** 20 dB bandwidth compliance  
**RF‑TX‑11:** In‑band spurious emissions  
**RF‑TX‑12:** Out‑of‑band spurious emissions  
**RF‑TX‑13:** Adjacent channel power (ACP)  
**RF‑TX‑14:** Carrier drift over time (1‑hour TX)  
**RF‑TX‑15:** TX stability across temperature (−40/25/85°C)

**RF‑RX‑01:** Receiver sensitivity at 1M PHY  
**RF‑RX‑02:** Receiver sensitivity at 2M PHY  
**RF‑RX‑03:** Receiver sensitivity at Coded PHY  
**RF‑RX‑04:** PER vs input power curve  
**RF‑RX‑05:** Blocking performance with CW interferer  
**RF‑RX‑06:** Co‑channel interference with another BLE device  
**RF‑RX‑07:** Adjacent channel interference with BLE  
**RF‑RX‑08:** WiFi coexistence—throughput under heavy WiFi  
**RF‑RX‑09:** Microwave oven interference robustness  
**RF‑RX‑10:** RX performance across temperature extremes  

(≈25 cases so far)

---

## 2. Advertising & scanning test cases

**ADV‑01:** Legacy advertising on all 3 channels  
**ADV‑02:** Advertising interval accuracy (e.g., 100 ms)  
**ADV‑03:** Advertising with different payload sizes (small/medium/max)  
**ADV‑04:** Non‑connectable advertising (ADV_NONCONN_IND)  
**ADV‑05:** Scannable advertising (ADV_SCAN_IND)  
**ADV‑06:** Directed advertising (high duty cycle)  
**ADV‑07:** Directed advertising (low duty cycle)  
**ADV‑08:** Extended advertising—single AUX chain  
**ADV‑09:** Extended advertising—multiple AUX chains  
**ADV‑10:** Periodic advertising—basic reception  
**ADV‑11:** Periodic advertising—loss and resync  
**ADV‑12:** Advertising channel map correctness (1, 2, 3, combinations)  
**ADV‑13:** Advertising with whitelist enabled  
**ADV‑14:** Advertising with blacklist (reject specific peer)  
**ADV‑15:** Advertising stop/start behavior under rapid toggling  

**SCAN‑01:** Passive scanning—discover DUT  
**SCAN‑02:** Active scanning—scan response correctness  
**SCAN‑03:** Duplicate filtering enabled  
**SCAN‑04:** Duplicate filtering disabled  
**SCAN‑05:** Scan window/interval boundary behavior  
**SCAN‑06:** Scan with whitelist filter  
**SCAN‑07:** Scan in presence of many advertisers (crowded air)  

(≈47 cases total)

---

## 3. Connection establishment & link layer procedures

**CONN‑EST‑01:** Central connects to advertising DUT (1M PHY)  
**CONN‑EST‑02:** Central connects using 2M PHY from start  
**CONN‑EST‑03:** Central connects using Coded PHY from start  
**CONN‑EST‑04:** Connection latency (time from CONNECT_IND to first data)  
**CONN‑EST‑05:** Connection timeout if DUT stops advertising mid‑procedure  
**CONN‑EST‑06:** Reconnect after DUT power cycle (bonded)  
**CONN‑EST‑07:** Reconnect after DUT power cycle (unbonded)  
**CONN‑EST‑08:** Connection with random device address  
**CONN‑EST‑09:** Connection with public device address  
**CONN‑EST‑10:** Connection with privacy (RPA rotation)  

**CONN‑PAR‑01:** Connection parameter update—shorter interval  
**CONN‑PAR‑02:** Connection parameter update—longer interval  
**CONN‑PAR‑03:** Connection parameter update—higher latency  
**CONN‑PAR‑04:** Connection parameter update—supervision timeout change  
**CONN‑PAR‑05:** Reject invalid connection parameters (out of spec)  
**CONN‑PAR‑06:** Host‑initiated vs peripheral‑initiated parameter update  
**CONN‑PAR‑07:** Multiple parameter updates in quick succession  

**PHY‑UPD‑01:** 1M → 2M PHY update during idle  
**PHY‑UPD‑02:** 1M → 2M PHY update during data transfer  
**PHY‑UPD‑03:** 1M → Coded PHY update  
**PHY‑UPD‑04:** Coded → 2M PHY update  
**PHY‑UPD‑05:** Request unsupported PHY and verify rejection  

(≈72 cases total)

---

## 4. GAP role behavior

**GAP‑PER‑01:** Peripheral role—start/stop advertising via API  
**GAP‑PER‑02:** Peripheral—handle multiple central connection attempts (if limited to 1)  
**GAP‑PER‑03:** Peripheral—disconnect reason codes (local vs remote)  
**GAP‑PER‑04:** Peripheral—bonding retention after reset  
**GAP‑PER‑05:** Peripheral—bonding retention after firmware update (if supported)  

**GAP‑CENT‑01:** Central role—scan and connect to known peripheral  
**GAP‑CENT‑02:** Central—connect to multiple peripherals concurrently (if supported)  
**GAP‑CENT‑03:** Central—connection priority switching between peripherals  
**GAP‑CENT‑04:** Central—whitelist‑only connections  
**GAP‑CENT‑05:** Central—auto‑reconnect to bonded peripheral  

(≈82 cases total)

---

## 5. GATT services, characteristics, MTU, notifications

**GATT‑DISC‑01:** Discover all primary services  
**GATT‑DISC‑02:** Discover included services  
**GATT‑DISC‑03:** Discover all characteristics of a service  
**GATT‑DISC‑04:** Discover descriptors of a characteristic  

**GATT‑RW‑01:** Read characteristic (short value)  
**GATT‑RW‑02:** Read characteristic (long value with Read Blob)  
**GATT‑RW‑03:** Write without response (short value)  
**GATT‑RW‑04:** Write with response (short value)  
**GATT‑RW‑05:** Long write using Prepare/Execute Write  
**GATT‑RW‑06:** Write invalid handle (expect error)  
**GATT‑RW‑07:** Read with insufficient authentication (expect error)  
**GATT‑RW‑08:** Read with insufficient authorization (expect error)  

**GATT‑MTU‑01:** MTU negotiation—central requests larger MTU  
**GATT‑MTU‑02:** MTU negotiation—peripheral limits MTU  
**GATT‑MTU‑03:** Data transfer at max MTU (throughput check)  

**GATT‑NOTIF‑01:** Enable notifications via CCCD  
**GATT‑NOTIF‑02:** Disable notifications via CCCD  
**GATT‑NOTIF‑03:** Notification burst at high rate (throughput)  
**GATT‑NOTIF‑04:** Indications with proper confirmation handling  
**GATT‑NOTIF‑05:** Behavior when peer does not confirm indication  

**GATT‑CUST‑01:** Custom service UUID correctness  
**GATT‑CUST‑02:** Endianness and field alignment in custom characteristic  
**GATT‑CUST‑03:** Boundary values for custom characteristic (min/max)  
**GATT‑CUST‑04:** Invalid value rejected by application logic  

(≈104 cases total)

---

## 6. Security: pairing, bonding, encryption, MITM

**SEC‑PAIR‑01:** Just Works pairing (no MITM)  
**SEC‑PAIR‑02:** Passkey Entry—DUT displays passkey  
**SEC‑PAIR‑03:** Passkey Entry—DUT inputs passkey  
**SEC‑PAIR‑04:** Numeric Comparison—user confirms match  
**SEC‑PAIR‑05:** OOB pairing (if supported)  
**SEC‑PAIR‑06:** Pairing failure—user rejects on one side  
**SEC‑PAIR‑07:** Pairing failure—timeout  

**SEC‑BOND‑01:** Bonding—keys stored after pairing  
**SEC‑BOND‑02:** Bonding—reconnect uses stored keys (no re‑pair)  
**SEC‑BOND‑03:** Bond deletion via API  
**SEC‑BOND‑04:** Bond deletion via factory reset  

**SEC‑ENC‑01:** Start encryption on existing connection  
**SEC‑ENC‑02:** Encryption pause/resume (if supported)  
**SEC‑ENC‑03:** Key refresh procedure  

**SEC‑MITM‑01:** Attempt to use wrong LTK (expect link termination)  
**SEC‑MITM‑02:** Replay old pairing data (expect failure)  

(≈120 cases total)

---

## 7. Power, sleep, and long‑duration behavior

**PWR‑ADV‑01:** Average current in advertising at 100 ms interval  
**PWR‑ADV‑02:** Average current in advertising at 1 s interval  
**PWR‑ADV‑03:** Power with extended advertising enabled  

**PWR‑CONN‑01:** Power at short interval (7.5 ms)  
**PWR‑CONN‑02:** Power at long interval (400 ms)  
**PWR‑CONN‑03:** Power with high slave latency  

**PWR‑SLEEP‑01:** Idle current in system sleep  
**PWR‑SLEEP‑02:** Wake‑up time from sleep to first advertisement  
**PWR‑SLEEP‑03:** Sleep entry/exit correctness under repeated cycles  

**PWR‑LONG‑01:** 24‑hour continuous connection with periodic notifications  
**PWR‑LONG‑02:** 7‑day periodic advertising battery drain profile  

(≈132 cases total)

---

## 8. Stress, negative, OTA, environment

**STRESS‑CONN‑01:** 10,000 connect/disconnect cycles with single peer  
**STRESS‑CONN‑02:** Rapid connect/disconnect with multiple peers  
**STRESS‑DATA‑01:** Continuous high‑rate notifications for 1 hour  
**STRESS‑PHY‑01:** Repeated PHY updates under traffic  

**NEG‑LL‑01:** Invalid LL control opcode (expect proper error/termination)  
**NEG‑LL‑02:** Invalid connection parameters (out of spec)  
**NEG‑GATT‑01:** Accessing non‑existent handle  
**NEG‑GATT‑02:** Writing value exceeding max length  
**NEG‑SEC‑01:** Pairing with unsupported IO capabilities combination  
**NEG‑SEC‑02:** Encryption request without prior pairing  

**OTA‑01:** Start OTA update over BLE  
**OTA‑02:** Power loss mid‑OTA—rollback behavior  
**OTA‑03:** OTA image with bad CRC—rejection  
**OTA‑04:** Version downgrade attempt—policy behavior  

**ENV‑01:** Full functional test at −40°C  
**ENV‑02:** Full functional test at +85°C  
**ENV‑03:** RF performance vs temperature sweep  
**ENV‑04:** Voltage variation (min/max supply) during active connection  

(≈150+ distinct test cases total)

---

If you’d like, next step I can:

- Turn this into a **traceable matrix** (Req ↔ TC IDs), or  
- Pick one area (e.g., **Security** or **GATT**) and expand each test into **full step/expected/result templates** in your preferred style.
