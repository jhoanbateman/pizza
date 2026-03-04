/**
 * @license
 * SPDX-License-Identifier: Apache-2.0
 */

import React, { useMemo, useEffect, useRef, useState } from 'react';
import { motion, AnimatePresence } from 'motion/react';
import { Rocket, Pizza, Trophy, Star, TrendingUp, Users, CheckCircle2, AlertCircle, Clock, Volume2 } from 'lucide-react';

// ==========================================
// 🚀 CORE METRICS (MANUAL UPDATES HERE)
// ==========================================
const CURRENT_MX_SMILEY = 88.9; 
const CURRENT_IA_SMILEY = 88.9; 
const TOTAL_SURVEYS_RECEIVED = 19; // Based on image grand total

const MX_GOAL = 83.0;
const IA_GOAL = 85.0;

const LEADERBOARD_DATA = [
  { name: "Oriana Patricia Gonzalez Escobar", count: 4, rate: "100%" },
  { name: "Mari Quevedo", count: 3, rate: "100%" },
  { name: "Alejandro Caicedo", count: 2, rate: "66.67%" },
  { name: "Julian Alfonso", count: 2, rate: "100%" },
  { name: "Cristian Galvis", count: 1, rate: "100%" },
  { name: "Jhoan Orozco", count: 1, rate: "100%" },
  { name: "Juan Martínez", count: 1, rate: "100%" },
  { name: "Sebastián Vélez", count: 1, rate: "100%" },
  { name: "Veronica Castillo", count: 1, rate: "50%" },
  { name: "", count: 0, rate: "" }, // 10th place empty
];

// Sound URLs
const SOUNDS = {
  ding: 'https://assets.mixkit.co/active_storage/sfx/2869/2869-preview.mp3',
  whoosh: 'https://assets.mixkit.co/active_storage/sfx/2571/2571-preview.mp3',
  chime: 'https://assets.mixkit.co/active_storage/sfx/2019/2019-preview.mp3'
};

// Rocket with Flame Component
const RocketWithFlame = ({ color, progress, isLaunching }: { color: string, progress: number, isLaunching: boolean }) => {
  return (
    <motion.div 
      initial={{ bottom: "0%" }}
      animate={{ bottom: `${progress}%` }}
      transition={{ duration: 2.5, ease: "easeInOut" }}
      className="absolute left-1/2 -translate-x-1/2 z-20"
    >
      <motion.div
        animate={isLaunching ? { 
          x: [-1, 1, -1, 1, 0],
          y: [0, -2, 0],
          rotate: [45, 43, 47, 45]
        } : {
          y: [0, -1, 0],
          rotate: [45, 44, 46, 45]
        }}
        transition={{ repeat: Infinity, duration: isLaunching ? 0.1 : 0.3 }}
        className="relative"
      >
        <Rocket className="w-10 h-10 text-white fill-white drop-shadow-[0_0_15px_rgba(255,255,255,0.5)]" />
        
        {/* Animated Flame */}
        <motion.div 
          animate={{ 
            scaleY: isLaunching ? [1.5, 2.5, 1.8, 2.2, 1.5] : [1, 1.3, 1.1, 1.4, 1],
            opacity: [0.8, 1, 0.9, 1, 0.8]
          }}
          transition={{ repeat: Infinity, duration: 0.08 }}
          className="absolute -bottom-6 left-1/2 -translate-x-1/2 w-4 h-10 origin-top"
        >
          <div className={`w-full h-full bg-gradient-to-b from-white via-${color} to-transparent blur-[2px] rounded-full shadow-[0_5px_15px_rgba(255,255,255,0.3)]`} 
               style={{ backgroundColor: color === 'emerald-400' ? '#10b981' : '#f97316' }} />
        </motion.div>
      </motion.div>
    </motion.div>
  );
};

// Smoke Effect Component
const LaunchSmoke = () => {
  return (
    <div className="absolute bottom-0 left-0 right-0 h-12 overflow-hidden pointer-events-none">
      {[...Array(6)].map((_, i) => (
        <motion.div
          key={i}
          initial={{ opacity: 0, scale: 0, y: 10 }}
          animate={{ 
            opacity: [0, 0.4, 0],
            scale: [1, 2, 2.5],
            y: [-10, -40],
            x: (i - 2.5) * 15
          }}
          transition={{ 
            repeat: Infinity, 
            duration: 1.5, 
            delay: i * 0.2,
            ease: "easeOut"
          }}
          className="absolute bottom-0 left-1/2 w-8 h-8 bg-white/10 blur-md rounded-full"
        />
      ))}
    </div>
  );
};

export default function App() {
  const audioRefs = useRef<{ [key: string]: HTMLAudioElement }>({});
  const [isLaunching, setIsLaunching] = useState(false);
  const [displayMX, setDisplayMX] = useState(0);
  const [displayIA, setDisplayIA] = useState(0);

  const mxTarget = Math.min(100, (CURRENT_MX_SMILEY / MX_GOAL) * 100);
  const iaTarget = Math.min(100, (CURRENT_IA_SMILEY / IA_GOAL) * 100);

  // Initialize sounds
  useEffect(() => {
    Object.entries(SOUNDS).forEach(([key, url]) => {
      const audio = new Audio(url);
      audio.volume = 0.3;
      audioRefs.current[key] = audio;
    });
  }, []);

  // Trigger Launch Animation
  useEffect(() => {
    const timer = setTimeout(() => {
      setIsLaunching(true);
      setDisplayMX(mxTarget);
      setDisplayIA(iaTarget);
      playSound('whoosh');
      
      // Stop "intense" launch mode after animation finishes
      setTimeout(() => setIsLaunching(false), 2500);
      setTimeout(() => playSound('chime'), 1500);
      
      if (CURRENT_MX_SMILEY >= MX_GOAL && CURRENT_IA_SMILEY >= IA_GOAL) {
        setTimeout(() => playSound('ding'), 2800);
      }
    }, 800);
    
    return () => clearTimeout(timer);
  }, [mxTarget, iaTarget]);

  const playSound = (key: keyof typeof SOUNDS) => {
    const audio = audioRefs.current[key];
    if (audio) {
      audio.currentTime = 0;
      audio.play().catch(() => {});
    }
  };

  // Math: Calculate consecutive smileys needed for IA (the harder goal)
  const smileysNeeded = useMemo(() => {
    const currentSmileys = (CURRENT_IA_SMILEY / 100) * TOTAL_SURVEYS_RECEIVED;
    const target = IA_GOAL / 100;
    
    if (CURRENT_IA_SMILEY >= IA_GOAL) return 0;
    
    const x = (target * TOTAL_SURVEYS_RECEIVED - currentSmileys) / (1 - target);
    return Math.ceil(x);
  }, []);

  const getStatus = () => {
    const avg = (CURRENT_MX_SMILEY + CURRENT_IA_SMILEY) / 2;
    if (CURRENT_MX_SMILEY >= MX_GOAL && CURRENT_IA_SMILEY >= IA_GOAL) {
      return {
        text: "🟢 DOUBLE GOAL SECURED! PIZZA FEAST TIME! 🍕🍕",
        color: "text-emerald-400",
        bg: "bg-emerald-500/10",
        border: "border-emerald-500/30"
      };
    }
    if (avg >= 80) {
      return {
        text: "🟡 So close! The oven is warming up...",
        color: "text-orange-400",
        bg: "bg-orange-400/10",
        border: "border-orange-400/30"
      };
    }
    return {
      text: "🔴 We are far from the pizza! Let's push!",
      color: "text-red-500",
      bg: "bg-red-500/10",
      border: "border-red-500/30"
    };
  };

  const status = getStatus();
  const mxProgress = Math.min(100, (CURRENT_MX_SMILEY / MX_GOAL) * 100);
  const iaProgress = Math.min(100, (CURRENT_IA_SMILEY / IA_GOAL) * 100);

  return (
    <div className="min-h-screen bg-[#050505] text-white font-['Inter',sans-serif] p-6 lg:p-10 overflow-x-hidden">
      {/* Background Glows */}
      <div className="fixed top-0 left-0 w-full h-full pointer-events-none overflow-hidden z-0">
        <div className="absolute top-[-10%] right-[-10%] w-[50%] h-[50%] bg-[#008060]/10 blur-[120px] rounded-full" />
        <div className="absolute bottom-[-10%] left-[-10%] w-[50%] h-[50%] bg-[#ff9100]/10 blur-[120px] rounded-full" />
      </div>

      <div className="relative z-10 max-w-7xl mx-auto space-y-8">
        {/* Header */}
        <motion.div 
          initial={{ opacity: 0, y: -20 }}
          animate={{ opacity: 1, y: 0 }}
          className="text-center space-y-2"
        >
          <h1 className="text-4xl md:text-6xl font-black tracking-tighter bg-clip-text text-transparent bg-gradient-to-r from-[#008060] via-white to-[#ff9100] drop-shadow-[0_0_15px_rgba(0,128,96,0.5)]">
            🚀 THE SMILEY CREW: PIZZA QUEST 🍕
          </h1>
          <div className="flex items-center justify-center gap-4 mt-4">
            <button 
              onClick={() => playSound('ding')}
              className="p-2 rounded-full bg-white/5 hover:bg-white/10 border border-white/10 transition-colors"
              title="Test Sound"
            >
              <Volume2 className="w-4 h-4 text-zinc-400" />
            </button>
            <p className="text-zinc-500 font-medium tracking-widest uppercase text-xs md:text-sm">
              Shopify Support Team • Dual Mission Target
            </p>
          </div>
        </motion.div>

        {/* Top Row: Rocket & Counter */}
        <div className="grid grid-cols-1 lg:grid-cols-3 gap-6">
          {/* Dual Metrics Progress Card */}
          <motion.div 
            initial={{ opacity: 0, x: -20 }}
            animate={{ opacity: 1, x: 0 }}
            className="lg:col-span-2 relative overflow-hidden rounded-3xl border border-white/10 bg-white/5 backdrop-blur-xl p-8"
          >
            <div className="flex justify-between items-start mb-8">
              <div>
                <h2 className="text-2xl font-bold flex items-center gap-2">
                  <TrendingUp className="text-[#008060]" />
                  Mission Status
                </h2>
                <p className="text-zinc-400 text-sm">Tracking MX and IA Goals</p>
              </div>
            </div>

            <div className="grid grid-cols-2 gap-8 h-[350px]">
              {/* MX Smiley Vertical Track */}
              <div className="flex flex-col items-center h-full space-y-4">
                <div className="flex-1 w-24 relative bg-black/40 rounded-full border border-white/5 p-1 overflow-visible">
                  {/* Goal Line */}
                  <div className="absolute bottom-[100%] left-0 right-0 border-t border-dashed border-[#008060]/50 text-[10px] text-[#008060] text-center pb-1">GOAL</div>
                  
                  {/* Progress Fill */}
                  <motion.div 
                    initial={{ height: 0 }}
                    animate={{ height: `${displayMX}%` }}
                    transition={{ duration: 2.5, ease: "easeInOut" }}
                    className="absolute bottom-0 left-0 right-0 bg-gradient-to-t from-[#008060]/30 to-transparent rounded-full" 
                  />
                  
                  {/* Smoke */}
                  {isLaunching && <LaunchSmoke />}
                  
                  {/* Rocket */}
                  <RocketWithFlame color="emerald-400" progress={displayMX} isLaunching={isLaunching} />
                </div>
                <div className="text-center">
                  <motion.div 
                    initial={{ opacity: 0 }}
                    animate={{ opacity: 1 }}
                    className="text-3xl font-black text-[#008060]"
                  >
                    {CURRENT_MX_SMILEY}%
                  </motion.div>
                  <div className="text-[10px] font-bold text-zinc-500 uppercase tracking-widest">MX Smiley</div>
                </div>
              </div>

              {/* IA Smiley Vertical Track */}
              <div className="flex flex-col items-center h-full space-y-4">
                <div className="flex-1 w-24 relative bg-black/40 rounded-full border border-white/5 p-1 overflow-visible">
                  {/* Goal Line */}
                  <div className="absolute bottom-[100%] left-0 right-0 border-t border-dashed border-[#ff9100]/50 text-[10px] text-[#ff9100] text-center pb-1">GOAL</div>
                  
                  {/* Progress Fill */}
                  <motion.div 
                    initial={{ height: 0 }}
                    animate={{ height: `${displayIA}%` }}
                    transition={{ duration: 2.5, ease: "easeInOut" }}
                    className="absolute bottom-0 left-0 right-0 bg-gradient-to-t from-[#ff9100]/30 to-transparent rounded-full" 
                  />

                  {/* Smoke */}
                  {isLaunching && <LaunchSmoke />}
                  
                  {/* Rocket */}
                  <RocketWithFlame color="orange-400" progress={displayIA} isLaunching={isLaunching} />
                </div>
                <div className="text-center">
                  <motion.div 
                    initial={{ opacity: 0 }}
                    animate={{ opacity: 1 }}
                    className="text-3xl font-black text-[#ff9100]"
                  >
                    {CURRENT_IA_SMILEY}%
                  </motion.div>
                  <div className="text-[10px] font-bold text-zinc-500 uppercase tracking-widest">IA Smiley</div>
                </div>
              </div>
            </div>
          </motion.div>

          {/* Smileys Needed Card */}
          <motion.div 
            initial={{ opacity: 0, x: 20 }}
            animate={{ opacity: 1, x: 0 }}
            className="rounded-3xl border border-white/10 bg-white/5 backdrop-blur-xl p-8 flex flex-col justify-center items-center text-center space-y-4"
          >
            <div className="p-4 rounded-2xl bg-[#ff9100]/20 border border-[#ff9100]/30">
              <Star className="w-8 h-8 text-[#ff9100] fill-[#ff9100]" />
            </div>
            <div>
              <div className="text-6xl font-black text-white">{smileysNeeded}</div>
              <div className="text-sm font-bold text-[#ff9100] uppercase tracking-widest mt-2">
                Consecutive Smileys Needed
              </div>
              <p className="text-zinc-500 text-xs mt-4 max-w-[200px] mx-auto">
                To maintain the {IA_GOAL}% IA goal based on current volume.
              </p>
            </div>
          </motion.div>
        </div>

        {/* Middle Row: Status Message */}
        <motion.div 
          initial={{ opacity: 0, scale: 0.95 }}
          animate={{ opacity: 1, scale: 1 }}
          className={`rounded-3xl border ${status.border} ${status.bg} p-8 text-center shadow-2xl`}
        >
          <h3 className={`text-2xl md:text-4xl font-black ${status.color} flex items-center justify-center gap-4`}>
            {CURRENT_IA_SMILEY >= IA_GOAL && CURRENT_MX_SMILEY >= MX_GOAL ? <CheckCircle2 className="w-10 h-10" /> : <AlertCircle className="w-10 h-10" />}
            {status.text}
          </h3>
        </motion.div>

        {/* Bottom Row: Leaderboard & Pizza Progress */}
        <div className="grid grid-cols-1 lg:grid-cols-2 gap-6">
          {/* Leaderboard */}
          <motion.div 
            initial={{ opacity: 0, y: 20 }}
            animate={{ opacity: 1, y: 0 }}
            className="rounded-3xl border border-white/10 bg-white/5 backdrop-blur-xl p-8"
          >
            <div className="flex items-center justify-between mb-6">
              <h2 className="text-2xl font-bold flex items-center gap-2">
                <Trophy className="text-yellow-500" />
                Top 10 Performers
              </h2>
              <Users className="text-zinc-500 w-5 h-5" />
            </div>

            <div className="space-y-2">
              {LEADERBOARD_DATA.map((user, index) => (
                <motion.div 
                  key={user.name || `empty-${index}`}
                  initial={{ opacity: 0, x: -10 }}
                  animate={{ opacity: 1, x: 0 }}
                  transition={{ delay: index * 0.05 }}
                  className={`flex items-center justify-between p-3 rounded-xl border ${
                    index === 0 && user.name ? 'border-yellow-500/50 bg-yellow-500/5 shadow-[0_0_15px_rgba(234,179,8,0.1)]' : 'border-white/5 bg-black/20'
                  } ${!user.name ? 'opacity-30 border-dashed' : ''}`}
                >
                  <div className="flex items-center gap-4 overflow-hidden">
                    <div className="w-8 text-center font-bold text-zinc-500 flex-shrink-0">
                      {index === 0 ? '🥇' : index === 1 ? '🥈' : index === 2 ? '🥉' : index + 1}
                    </div>
                    <div className="font-semibold text-zinc-200 truncate pr-2">
                      {user.name || "Awaiting Champion..."}
                    </div>
                  </div>
                  {user.name && (
                    <div className="flex items-center gap-4 flex-shrink-0">
                      <div className="text-right">
                        <div className="text-sm font-black text-white">{user.count} Smileys</div>
                        <div className="text-[10px] text-zinc-500 uppercase tracking-tighter">{user.rate} Rate</div>
                      </div>
                      <Star className="w-4 h-4 text-yellow-500 fill-yellow-500" />
                    </div>
                  )}
                </motion.div>
              ))}
            </div>
          </motion.div>

          {/* Pizza Progress Visual */}
          <motion.div 
            initial={{ opacity: 0, y: 20 }}
            animate={{ opacity: 1, y: 0 }}
            className="rounded-3xl border border-white/10 bg-white/5 backdrop-blur-xl p-8 flex flex-col items-center justify-center text-center space-y-8"
          >
            <h2 className="text-2xl font-bold">Pizza Party Status</h2>
            
            <div className="relative w-64 h-64">
              <div className="absolute inset-0 rounded-full border-8 border-orange-900/30 bg-orange-900/10" />
              <svg viewBox="0 0 100 100" className="w-full h-full -rotate-90">
                <circle
                  cx="50"
                  cy="50"
                  r="40"
                  fill="transparent"
                  stroke="#ff9100"
                  strokeWidth="8"
                  strokeDasharray={`${iaProgress * 2.51} 251`}
                  className="transition-all duration-1000 ease-out"
                />
              </svg>
              <div className="absolute inset-0 flex items-center justify-center">
                <motion.div
                  animate={{ scale: [1, 1.1, 1] }}
                  transition={{ repeat: Infinity, duration: 3 }}
                >
                  <Pizza className="w-24 h-24 text-[#ff9100] drop-shadow-[0_0_20px_rgba(255,145,0,0.4)]" />
                </motion.div>
              </div>
            </div>

            <div className="space-y-2">
              <div className="text-3xl font-black text-emerald-400">GOALS MET!</div>
              <div className="text-sm text-zinc-500 uppercase tracking-widest">The Oven is Blazing</div>
              <div className="flex items-center gap-2 text-zinc-400 text-sm mt-4">
                <Clock className="w-4 h-4" />
                <span>Last updated: {new Date().toLocaleTimeString()}</span>
              </div>
            </div>
          </motion.div>
        </div>
      </div>

      <div className="mt-12 text-center text-zinc-600 text-xs uppercase tracking-[0.2em]">
        Designed for The Smiley Crew • Built with Precision
      </div>
    </div>
  );
}
