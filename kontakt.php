<?php
/* ─────────────────────────────────────────────────────────────
   İletişim formu → e-posta (Bahar Sonek)
   Gereksinim: PHP destekli hosting (ör. IONOS, Strato, All-Inkl, Hostinger).
   AYARLAR: Alıcı adresi ve gönderen adresi aşağıda.
   GONDEREN: Sitenin kendi alan adından bir adres olmalı (ör. info@baharsonek.de),
   aksi halde e-postalar spam klasörüne düşebilir.
   ───────────────────────────────────────────────────────────── */
$ALICI    = 'baharsonek.official@gmail.com';
$GONDEREN = 'noreply@' . preg_replace('/^www\./', '', $_SERVER['SERVER_NAME'] ?? 'localhost');

$lang  = (($_POST['lang'] ?? 'tr') === 'de') ? 'de' : 'tr';
$geri  = $lang === 'de' ? 'de/kontakt.html' : 'iletisim.html';
$taban = rtrim(dirname($_SERVER['SCRIPT_NAME']), '/\\');
function don($url) { header('Location: ' . $url); exit; }

if ($_SERVER['REQUEST_METHOD'] !== 'POST') don("$taban/$geri");

// Spam koruması: gizli alan doluysa sessizce "başarılı" göster
if (!empty($_POST['website'])) don("$taban/$geri?gonderildi=1#form");

$temiz = fn($k, $max = 200) => trim(mb_substr(str_replace(["\r", "\n"], ' ', strip_tags($_POST[$k] ?? '')), 0, $max));
$ad    = $temiz('ad');
$tel   = $temiz('tel', 60);
$email = filter_var(trim($_POST['email'] ?? ''), FILTER_VALIDATE_EMAIL);
$konu  = $temiz('konu', 120);
$mesaj = trim(mb_substr(strip_tags($_POST['mesaj'] ?? ''), 0, 5000));

if ($ad === '' || $tel === '' || !$email || $mesaj === '') don("$taban/$geri?hata=1#form");

$baslik = ($lang === 'de' ? 'Kontaktanfrage' : 'Web sitesi mesajı') . ": $konu – $ad";
$govde  = "Web sitesi iletişim formu / Kontaktformular\n"
        . "──────────────────────────────\n"
        . "Ad Soyad / Name: $ad\n"
        . "Telefon:         $tel\n"
        . "E-posta / E-Mail: $email\n"
        . "Konu / Betreff:  $konu\n"
        . "Dil / Sprache:   " . strtoupper($lang) . "\n"
        . "──────────────────────────────\n\n"
        . $mesaj . "\n";

$basliklar = [
  'From: Bahar Sonek Web <' . $GONDEREN . '>',
  'Reply-To: ' . $email,
  'MIME-Version: 1.0',
  'Content-Type: text/plain; charset=UTF-8',
  'Content-Transfer-Encoding: 8bit',
];
$ok = mail($ALICI, '=?UTF-8?B?' . base64_encode($baslik) . '?=', $govde, implode("\r\n", $basliklar));

don("$taban/$geri?" . ($ok ? 'gonderildi=1' : 'hata=1') . '#form');
