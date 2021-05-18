# Installation

Before using Alexandria, you need to have two services running:
`grobid` (used for processing pdf files) and `mongodb`.


### Grobid

You first need to have an instance of [`grobid`](https://grobid.readthedocs.io/en/latest/) running.

Using Docker:
```
docker run -t --rm --init -p 8080:8070 -p 8081:8071 lfoppiano/grobid:0.6.2
```
The above command will download the image and run it.
(Add `-d` to run in daemon mode.)

Verify that `grobid` is running at http://localhost:8070.


If you configure `grobid` to listen on a different host/port, please adapt
the `grobid.json` configuration.

### Mongodb

Alexandria requires you to have a mongodb instance running
locally at the standard port (`27017`).

Using docker:

```
docker run -p 27017:27017 mongo
```
(Add `-d` to run in daemon mode.)

### Alexandria

You're now ready to install Alexandria.

```
git clone https://github.com/AdaLogics/paper-analyser
git submodule init
git submodule update
cd paper-analyser/alexandria
python3 -m venv venv
. venv/bin/activate
pip install -r ../requirements.txt
cd grobid_client
pip install .
cd ..
```


# Usage

To process the pdf files in `example-papers` launch:

```
python runner.py ../example-papers
```

<details>
  <summary>Click to see the output.</summary>

```
Please check out the script for more info.
GROBID server is up and running
Connecting to db.
Processing files in ../example-papers/
Parsing 1908.09204.pdf
Title: RePEconstruct: reconstructing binaries with self-modifying code and import address table destruction
Authors: David Korczynski
References:
Title: System-Level Support for Intrusion Recovery
Authors: Andrei Bacs, Remco Vermeulen, Asia Slowinska, Herbert Bos
-------------------
Title: WYSINWYX: What You See Is Not What You eXecute
Authors: G Balakrishnan, T Reps, D Melski, T Teitelbaum
-------------------
Title: BYTEWEIGHT: Learning to Recognize Functions in Binary Code
Authors: Bao Ti Any, Jonathan Burket, Maverick Woo, Rafael Turner, David Brumley
-------------------
Title: incy: Detecting Host-Based Code Injection A acks in Memory Dumps
Authors: Niklas Omas Barabosch, Adrian Bergmann, Elmar Dombeck, Padilla
-------------------
Title: Bee Master: Detecting Host-Based Code Injection A acks
Authors: Sebastian Barabosch, Elmar Eschweiler, Gerhards-Padilla
-------------------
Title: CoDisasm: Medium Scale Concatic Disassembly of Self-Modifying Binaries with Overlapping Instructions
Authors: Guillaume Bonfante, Jose Fernandez, Jean-Yves Marion, Benjamin Rouxel
-------------------
Title: Minemu: e World's Fastest Taint Tracker
Authors: Erik Bosman, Asia Slowinska, Herbert Bos
-------------------
Title: Decoupling Dynamic Program Analysis from Execution in Virtual Environments
Authors: Jim Chow, Peter Chen
-------------------
Title: Decompilation of Binary Programs. So w
Authors: Cristina Cifuentes, K. John Gough
-------------------
Title: Ether: Malware Analysis via Hardware Virtualization Extensions
Authors: Artem Dinaburg, Paul Royal, Monirul Sharif, Wenke Lee
-------------------
Title: Repeatable Reverse Engineering with PANDA
Authors: Brendan Dolan-Gavi, Josh Hodosh, Patrick Hulin, Tim Leek, Ryan Whelan
-------------------
Title: Graph-based comparison of executable objects (english version)
Authors: Rolf Omas Dullien, Rolles
-------------------
Title: Signatures for Library Functions in Executable Files
Authors: Mike Van Emmerik
-------------------
Title: Structural Comparison of Executable Objects
Authors: ; Halvar Flake, G Sig Sidar, Workshop
-------------------
Title: A Study of the Packer Problem and Its Solutions
Authors: Fanglu Guo, Peter Ferrie, Tzi-Cker Chiueh
-------------------
Title: DECAF: A Platform-Neutral Whole-System Dynamic Binary Analysis Platform
Authors: Andrew Henderson, Lok-Kwong Yan, Xunchao Hu, Aravind Prakash, Heng Yin, Stephen Mccamant
-------------------
Title: MutantX-S: Scalable Malware Clustering Based on Static Features
Authors: Xin Hu, Sandeep Bhatkar, Kent Gri N, Kang Shin
-------------------
Title: 
Authors: Hungenberg, Eckert Ma Hias
-------------------
Title: malWASH: Washing Malware to Evade Dynamic Analysis
Authors: K Kyriakos, Mathias Ispoglou, Payer
-------------------
Title: Labeling Library Functions in Stripped Binaries
Authors: Emily Jacobson, Nathan Rosenblum, Barton Miller
-------------------
Title: Secure and advanced unpacking using computer emulation
Authors: Sébastien Josse
-------------------
Title: Malware Dynamic Recompilation
Authors: S Josse
-------------------
Title: Renovo: A Hidden Code Extractor for Packed Executables
Authors: Min Kang, Pongsin Poosankam, Heng Yin
-------------------
Title: Taint-assisted IAT Reconstruction against Position Obfuscation
Authors: Yuhei Kawakoya, Makoto Iwamura, Jun Miyoshi
-------------------
Title: API Chaser: Taint-Assisted Sandbox for Evasive Malware Analysis
Authors: Yuhei Kawakoya, Eitaro Shioji, Makoto Iwamura
-------------------
Title: Jakstab: A Static Analysis Platform for Binaries
Authors: Johannes Kinder, Helmut Veith
-------------------
Title: Power of Procrastination: Detection and Mitigation of Execution-stalling Malicious Code
Authors: Clemens Kolbitsch, Engin Kirda, Christopher Kruegel
-------------------
Title: RePEconstruct: reconstructing binaries with selfmodifying code and import address table destruction
Authors: David Korczynski
-------------------
Title: Capturing Malware Propagations with Code Injections and Code-Reuse A acks
Authors: David Korczynski, Heng Yin
-------------------
Title: Polymorphic Worm Detection Using Structural Information of Executables
Authors: Christopher Kruegel, Engin Kirda, Darren Mutz, William Robertson, Giovanni Vigna
-------------------
Title: Static Disassembly of Obfuscated Binaries
Authors: Christopher Kruegel, William Robertson, Fredrik Valeur, Giovanni Vigna
-------------------
Title: Graph Matching Networks for Learning the Similarity of Graph Structured Objects
Authors: Yujia Li, Chenjie Gu, Omas Dullien
-------------------
Title: OmniUnpack: Fast, Generic, and Safe Unpacking of Malware
Authors: L Martignoni, M Christodorescu, S Jha
-------------------
Title: Measuring and Defeating Anti-Instrumentation-Equipped Malware
Authors: Mario Polino, Andrea Continella, Sebastiano Mariani, Lorenzo Stefano D'alessio, Fabio Fontana, Stefano Gri, Zanero
-------------------
Title: Argos: an Emulator for Fingerprinting Zero-Day A acks
Authors: Georgios Portokalidis, Asia Slowinska, Herbert Bos
-------------------
Title: 
Authors: Symantec Security Response
-------------------
Title: Learning to Analyze Binary Computer Code
Authors: Nathan Rosenblum, Xiaojin Zhu, Barton Miller, Karen Hunt
-------------------
Title: PolyUnpack: Automating the Hidden-Code Extraction of Unpack-Executing Malware
Authors: Paul Royal, Mitch Halpin, David Dagon, Robert Edmonds, Wenke Lee
-------------------
Title: Eureka: A Framework for Enabling Static Malware Analysis
Authors: Monirul Sharif, Vinod Yegneswaran, Hassen Saidi, Phillip Porras, Wenke Lee
-------------------
Title: Binary Translation
Authors: Richard Sites, Anton Cherno, B Ma Hew, Maurice Kirk, Sco Marks, Robinson
-------------------
Title: DeepMem: Learning Graph Neural Network Models for Fast and Robust Memory Forensic Analysis
Authors: Wei Song, Chang Heng Yin, Dawn Liu, Song
-------------------
Title: SoK: Deep Packer Inspection: A Longitudinal Study of the Complexity of Run-Time Packers
Authors: Davide Xabier Ugarte-Pedrero, Igor Balzaro I, Pablo Santos, Bringas
-------------------
Title: Panorama: Capturing System-wide Information Flow for Malware Detection and Analysis
Authors: Dawn Heng Yin, Manuel Song, Christopher Egele, Engin Kruegel, Kirda
-------------------

Parsing 1908.10167.pdf
Title: RePEconstruct: reconstructing binaries with self-modifying code and import address table destruction
Authors: David Korczynski, Createprocessa, Createfilea, , 
References:
Title: System-Level Support for Intrusion Recovery
Authors: Andrei Bacs, Remco Vermeulen, Asia Slowinska, Herbert Bos
-------------------
Title: incy: Detecting Host-Based Code Injection A acks in Memory Dumps
Authors: Niklas Omas Barabosch, Adrian Bergmann, Elmar Dombeck, Padilla
-------------------
Title: Bee Master: Detecting Host-Based Code Injection A acks
Authors: Sebastian Barabosch, Elmar Eschweiler, Gerhards-Padilla
-------------------
Title: Host-based code injection a acks: A popular technique used by malware
Authors: Elmar Omas Barabosch, Gerhards-Padilla
-------------------
Title: A View on Current Malware Behaviors
Authors: Ulrich Bayer, Imam Habibi, Davide Balzaro I, Engin Kirda
-------------------
Title: Dynamic Analysis of Malicious Code
Authors: Ulrich Bayer, Andreas Moser, Christopher Kruegel, Engin Kirda
-------------------
Title: Dridex's Cold War
Authors: Magal Baz, Or Safran
-------------------
Title: QEMU, a Fast and Portable Dynamic Translator
Authors: Fabrice Bellard
-------------------
Title: CoDisasm: Medium Scale Concatic Disassembly of Self-Modifying Binaries with Overlapping Instructions
Authors: Guillaume Bonfante, Jose Fernandez, Jean-Yves Marion, Benjamin Rouxel
-------------------
Title: Understanding Linux Malware
Authors: E Cozzi, M Graziano, Y Fratantonio, D Balzaro I
-------------------
Title: Understanding Linux malware
Authors: Emanuele Cozzi, Mariano Graziano, Yanick Fratantonio, Davide Balzaro I
-------------------
Title: Ether: Malware Analysis via Hardware Virtualization Extensions
Authors: Artem Dinaburg, Paul Royal, Monirul Sharif, Wenke Lee
-------------------
Title: Repeatable Reverse Engineering with PANDA
Authors: Brendan Dolan-Gavi, Josh Hodosh, Patrick Hulin, Tim Leek, Ryan Whelan
-------------------
Title: A Survey on Automated Dynamic Malware-analysis Techniques and Tools
Authors: Manuel Egele, Engin Eodoor Scholte, Christopher Kirda, Kruegel
-------------------
Title: A Survey of Mobile Malware in the Wild
Authors: Adrienne Felt, Ma Hew Fini Er, Erika Chin, Steve Hanna, David Wagner
-------------------
Title: DECAF: A Platform-Neutral Whole-System Dynamic Binary Analysis Platform
Authors: Andrew Henderson, Lok-Kwong Yan, Xunchao Hu, Aravind Prakash, Heng Yin, Stephen Mccamant
-------------------
Title: Ten Process Injection Techniques: A Technical Survey Of Common And Trending Process Injection Techniques
Authors: Ashkan Hosseini
-------------------
Title: 
Authors: Hungenberg, Eckert Ma Hias
-------------------
Title: malWASH: Washing Malware to Evade Dynamic Analysis
Authors: K Kyriakos, Mathias Ispoglou, Payer
-------------------
Title: Renovo: A Hidden Code Extractor for Packed Executables
Authors: Min Kang, Pongsin Poosankam, Heng Yin
-------------------
Title: API Chaser: Taint-Assisted Sandbox for Evasive Malware Analysis
Authors: Yuhei Kawakoya, Eitaro Shioji, Makoto Iwamura
-------------------
Title: RePEconstruct: reconstructing binaries with selfmodifying code and import address table destruction
Authors: David Korczynski
-------------------
Title: Precise system-wide concatic malware unpacking. arXiv e-prints
Authors: David Korczynski
-------------------
Title: Capturing Malware Propagations with Code Injections and Code-Reuse A acks
Authors: David Korczynski, Heng Yin
-------------------
Title: 
Authors: Pasquale Giulio De
-------------------
Title: 
Authors: Daniel Plohmann, Martin Clauß, Elmar Padilla
-------------------
Title: Argos: an Emulator for Fingerprinting Zero-Day A acks
Authors: Georgios Portokalidis, Asia Slowinska, Herbert Bos
-------------------
Title: AVclass: A Tool for Massive Malware Labeling
Authors: Marcos Sebastián, Richard Rivera, Platon Kotzias, Juan Caballero
-------------------
Title: Malrec: Compact Full-Trace Malware Recording for Retrospective Deep Analysis
Authors: Giorgio Severi, Tim Leek, Brendan Dolan-Gavi
-------------------
Title: Nor Badrul Anuar, Rosli Salleh, and Lorenzo Cavallaro
Authors: Kimberly Tam, Ali Feizollah
-------------------
Title: SoK: Deep Packer Inspection: A Longitudinal Study of the Complexity of Run-Time Packers
Authors: Davide Xabier Ugarte-Pedrero, Igor Balzaro I, Pablo Santos, Bringas
-------------------
Title: Deep Ground Truth Analysis of Current Android Malware
Authors: Fengguo Wei, Yuping Li, Sankardas Roy, Xinming Ou, Wu Zhou
-------------------
Title: Panorama: Capturing System-wide Information Flow for Malware Detection and Analysis
Authors: Dawn Heng Yin, Manuel Song, Christopher Egele, Engin Kruegel, Kirda
-------------------
Title: Dissecting Android Malware: Characterization and Evolution
Authors: Yajin Zhou, Xuxian Jiang
-------------------
```
</details>

# Processing data

A simple example of how to process the data: [visualization.py](visualization.py).
